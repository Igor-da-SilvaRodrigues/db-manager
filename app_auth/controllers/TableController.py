from app_auth.Repositories.TableRepository import tableColumns
from app_auth.Services.NavbarService import NavbarService
from django.shortcuts import render
from django.db import connection
from pprint import pprint
from collections import defaultdict
from app_auth.Repositories.TableRepository import tableColumns


def showTable(request,schema, table):
    tc = tableColumns(schema, table)
    print([i for i in tc])
    context = {}
    context['tc'] = tc
    context['schemas'] = NavbarService.mount()
    return render(request, 'table.html', context)

