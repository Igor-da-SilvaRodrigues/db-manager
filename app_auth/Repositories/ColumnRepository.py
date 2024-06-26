from django.db import connections
from django.utils.connection import ConnectionProxy
from app_auth.Helpers.DB import makeConnection
from app_auth.Builders.ColumnBuilder import ColumnBuilder;


def createColumnByRequest(request):
    conection = makeConnection(request)
    cursor = conection.cursor();

    try:
        cursor.execute(ColumnBuilder(request).get());
    except Exception as exception:
        return {
            "type": 'error',
            "message": repr(exception)
        }

    return {
        "type": 'success',
        "message": "Success on create {} column.".format(request.POST.get('name'))
    }


def updateColumnByRequest(request):
    conection = makeConnection(request)
    cursor = conection.cursor();

    try:
        cursor.execute(ColumnBuilder(request).get());

        return {
            "type": 'success',
            "message": "Success on update {} column.".format(request.POST.get('old_name'))
        }
    except Exception as exception:
        return {
            "type": 'error',
            "message": repr(exception)
        }


def renameColumnByRequest(request):
    conection = makeConnection(request)
    cursor = conection.cursor();

    try:
        cursor.execute("ALTER TABLE {} RENAME COLUMN {} TO {};".format(
            request.POST.get('table'),
            request.POST.get('old_name'),
            request.POST.get('name'),
        ));
    except Exception as exception:
        return {
            "type": 'error',
            "message": repr(exception)
        }

    return {
        "type": 'success',
        "message": "Success on rename {} column.".format(request.POST.get('old_name'))
    }
