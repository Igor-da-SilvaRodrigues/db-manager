from app_auth.Services.NavbarService import NavbarService
from django.shortcuts import redirect, render

from app_auth.loginform import LoginForm
from app_auth.backends.MySqlBackend import static_authenticate
from app_auth.exceptions import UnauthorizedError, NetworkError
from app_auth.createdbform import CreateDbForm
from app_auth.sqlinputform import SqlInputForm

from app_auth.Services.SqlInputService import execute_sql

import traceback

class AuthController:
    
    
    def login(self, request):
        """View da pagina de login
        """
        context = {}
        form = LoginForm()
        context['form'] = form
        context['isUnauthorized'] = False
        context['isNetworkError'] = False
        context['isUnexpectedError'] = False
        
        if 'username' in request.session.keys():
            #redirect if already logged in
            return redirect("/db/manager")
        
        # Processing login request
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            host = request.POST["host"]
            port = request.POST["port"]
            try:
                static_authenticate(username=username, password=password, host=host, port=port)
                #If no errors were raised, user is authenticated
                #persist user info to request session
                request.session['username'] = username
                request.session['password'] = password
                request.session['host'] = host 
                request.session['port'] = port
                #redirect to dashboard
                return redirect("/db/manager")
            except UnauthorizedError:
                context['isUnauthorized'] = True
            except NetworkError:
                context['isNetworkError'] = True
            except Exception as ex:
                #Unexpected exception, log
                traceback.print_exc()
                context['isUnexpectedError'] = True
                
        return render(request, 'login.html', context)

    def dashboard(self, request):
        # Redirect anonymous users to log in page
        if 'username' not in request.session.keys():
            return redirect("/db/manager/login")
        
        context = {}
        form = CreateDbForm()
        context['new_db_form'] = form
        sql_form = SqlInputForm()
        context['sql_form'] = sql_form
        
        
        if request.method == "POST" and 'sql-input-form-button' in request.POST:
            #definindo texto inicial do formulário como o script inserido, para que não se perca a entrada do usuário
            context['sql_form'] = SqlInputForm(initial_text=request.POST["sql"])
            
            results = execute_sql(
                username    = request.session["username"],
                host        = request.session["host"],
                port        = request.session["port"],
                password    = request.session["password"],
                sql         = request.POST["sql"]
            )
            context['sql_results'] = results
            
        if request.method == "POST" and 'new-db-form-button' in request.POST:
            nome = request.POST["nome"]
            results = execute_sql(
                username    = request.session["username"],
                host        = request.session["host"],
                port        = request.session["port"],
                password    = request.session["password"],
                sql         = (f"CREATE SCHEMA {nome};")
            )            
            context['sql_results'] = results
            
        # montar o serviço de navbar por último, para refletir qualquer alteração no BD feita pelos comandos.
        context['schemas'] = NavbarService.mount()
        return render(request, 'dashboard.html', context)
