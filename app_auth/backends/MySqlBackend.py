from django.contrib.auth.base_user import AbstractBaseUser

from app_auth.models import User
from app_auth.exceptions import NetworkError, UnauthorizedError

import pymysql
    
def static_authenticate(
        username: str,
        password: str,
        host: str,
        port: str | int
        ) -> None:
    """Attempts to authenticate a user.


    Args:
        username (str): username
        password (str): password
        host (str): server hostname
        port (str | int): port number

    Raises:
        UnauthorizedError: If the credentials were invalid
        NetworkError: If unable to connect to server
    """
        
    try:
        #send user info to mysql so it tells us if the user is authenticated
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            port=int(port)
        )
        conn.close()
        # No error means user is authenticated

    except pymysql.OperationalError as ex:
            error_code = ex.args[0]
            match error_code:
                case 1045:
                    raise UnauthorizedError("Invalid credentials")
                case 2003:
                    raise NetworkError("Cannot connect to server")