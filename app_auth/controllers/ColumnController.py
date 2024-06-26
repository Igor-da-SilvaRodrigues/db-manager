from app_auth.Services.NavbarService import NavbarService
from django.shortcuts import redirect, render
from django.db import connection
import logging
from collections import defaultdict
import json;
from django.urls import reverse
from django.template.context_processors import request
from app_auth.Repositories.SchemaRepository import schemaTables;
from app_auth.Repositories.TableRepository import tableColumn;
from app_auth.Repositories.ColumnRepository import createColumnByRequest, updateColumnByRequest, renameColumnByRequest;
from app_auth.Builders.ColumnBuilder import ColumnBuilder;
import re


def showColumn(request, schema, table, column):
    result = tableColumn(schema, table, column);

    if (result == False):
        return render(request, '404.html');

    formated_columns = {
        "type": result[0][2].upper(),
        "options": None,
        "nullable": '0' if result[0][1] == 'NO' else '1',
        "default": result[0][0] or '',
        "max_length": result[0][3] or '',
        "pk": "1" if result[0][4] == 'PRI' else "0",
        "fk": "1" if result[0][7] != None else "0",
        "fk_table": result[0][7],
        "fk_column": result[0][8],
    }

    type = result[0][2].upper();

    if (type.startswith('ENUM') or type.startswith('SET')):
        formated_columns['type'] = type.split('(')[0];
        formated_columns['options'] = (type.split('('))[1].split(')')[0].replace('\'', '').split(',');
    elif('(' in type):
        formated_columns['type'] = type.split('(')[0];
    elif(' ' in type):
        formated_columns['type'] = type.split(' ')[0];

    return render(request, 'column.html', {
        'schemas': NavbarService.mount(),
        'schema': schema,
        'table': table,
        'column': column,
        'field_values': formated_columns,
        'table_columns': schemaTables(schema, True),
        'submit_endpoint': reverse('column.update'),
        'button_label': 'Update',
        'method': 'POST',
        'response': request.GET.get('message')
    })


def createColumn(request, schema, table):
    return render(request, 'column.html', {
        'schemas': NavbarService.mount(),
        'schema': schema,
        'table': table,
        'column': '',
        'field_values': {},
        'table_columns': schemaTables(schema, True),
        'submit_endpoint': reverse('column.store'),
        'button_label': 'Create',
        'method': 'POST',
    });


def updateColumn(request):
    response = updateColumnByRequest(request);

    if (response['type'] == 'success'):
        if (request.POST.get('old_name') != request.POST.get('name')):
            response = renameColumnByRequest(request);

    return render(request, 'column.html', {
        'schemas': NavbarService.mount(),
        'schema': request.POST.get('schema'),
        'table': request.POST.get('table'),
        'column': request.POST.get('name'),
        'field_values': {
            "type": request.POST.get('type'),
            "nullable": request.POST.get('nullable'),
            "default": request.POST.get('default'),
            "max_length": request.POST.get('max_length'),
            "pk": request.POST.get('pk'),
            "fk": request.POST.get('fk'),
            "fk_table": request.POST.get('fk_table'),
            "fk_column": request.POST.get('fk_column'),
        },
        'table_columns': schemaTables(request.POST.get('schema'), True),
        'submit_endpoint': reverse('column.update'),
        'button_label': 'Update',
        'method': 'POST',
        'response': response
    });


def storeColumn(request):
    response = createColumnByRequest(request);

    return redirect(reverse('column.show', kwargs={
        'schema': request.POST.get('schema'),
        'table': request.POST.get('table'),
        'column': request.POST.get('name'),
    }));
