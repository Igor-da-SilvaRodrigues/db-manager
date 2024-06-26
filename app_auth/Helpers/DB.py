import mysql.connector


def makeConnection(request):
    return mysql.connector.connect(
        database=request.POST.get('schema'),
        user=request.session.get('username', 'root'),
        password=request.session.get('password', ''),
        host=request.session.get('host', 'localhost'),
        port=request.session.get('port', 3306),
    );
