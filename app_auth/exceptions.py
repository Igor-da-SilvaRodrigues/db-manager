class UnauthorizedError(Exception):
    """User was not authorized, likely due to invalid credentials"""
    
class NetworkError(Exception):
    """Could not connect to the database"""
