from app_auth.Services.NavbarService import NavbarService
from django.shortcuts import render, redirect

from app_auth.Services.SchemaService import SchemaService
from app_auth.Services.SqlInputService import execute_sql

def show(request, schema=None):
    # Redirect anonymous users to log in page
    if 'username' not in request.session.keys():
        return redirect("/db/manager/login")
    
    context = {}
    
    # Dropping database
    if request.method == "POST" and 'drop-schema-button' in request.POST:
        results = execute_sql(
            username    = request.session["username"],
            host        = request.session["host"],
            port        = request.session["port"],
            password    = request.session["password"],
            sql         = (f"DROP DATABASE `{schema}`;")
        )
        print(results)
        # Redirect to dashboard
        return redirect("/db/manager")
    
    context['details'] = SchemaService.detail(schema)
    context['schemas'] = NavbarService.mount()
    return render(request, 'schema.html', context)
