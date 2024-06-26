import pymysql.cursors
import traceback
import sqlparse

def _split_sql_commands(sql_script):
    """Splits a sql script into a list of sql commands, ignoring any comments"""
    formatted_sql = sqlparse.format(sql_script, strip_comments=True)
    
    commands = sqlparse.split(formatted_sql, strip_semicolon=True)
    print(commands)
    return commands
    

def execute_sql(username: str, host: str, password: str, sql: str, port: str | int) -> list[object]:
    """Executa um ou mais comandos sql. Os comandos devem estar separados por ';' 

    Args:
        username (str): o nome de usuário
        host (str): o hostname do usuário
        password (str): a senha do usuário
        sql (str): o(s) comando(s) sql
        port (str | int) : A porta http
    Returns:
        list[object]: uma lista contendo os resultados
    """
    sql_commands = _split_sql_commands(sql)
    results = []
    try:
        connection = pymysql.connect(
            host=host,
            user=username,
            password=password,
            port=int(port),
            cursorclass=pymysql.cursors.DictCursor
        )
        
        
        with connection.cursor() as cursor:
            for command in sql_commands:
                
                result = {}

                try:
                    result["command"] = command
                    result["mog_command"] = cursor.mogrify(command)
                    result["affected_rows"] = cursor.execute(command)
                    results_of_command = cursor.fetchall()        
                    result_len = len(results_of_command)
                    result["results"] = results_of_command
                    result["result_len"] = result_len
                    result["headers"] = results_of_command[0].keys() if result_len > 0 else None
                    result["rows"] = [row.values() for row in results_of_command ] if result_len > 0 else None
                except pymysql.Error as ex:
                    result["is_error"] = True
                    result["error"] = str(ex)
                results.append(result)
                
        connection.commit()
    except pymysql.Error as ex:
        result = {}
        result["is_error"] = True
        result["error"] = str(ex)
        results.append(result)
        
        traceback.print_exc()
    
    return results
        