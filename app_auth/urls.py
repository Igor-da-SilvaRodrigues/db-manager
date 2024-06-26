from django.urls import path
from .controllers.AuthController import AuthController
from .controllers import SchemaController
from .controllers.TableController import showTable
from .controllers.ColumnController import storeColumn, updateColumn, showColumn, createColumn
authController = AuthController();

urlpatterns = [
    path('login/', authController.login),
    path('', authController.dashboard),
    path('schema/<str:schema>/', SchemaController.show, name="schema.show"),
    path('table/<str:schema>/<str:table>/', showTable, name="table.show"),
    path('column/<str:schema>/<str:table>/<str:column>/', showColumn, name="column.show"),
    path('column/<str:schema>/<str:table>/', createColumn, name="column.create"),
    path('column/update/', updateColumn, name="column.update"),
    path('column/store/', storeColumn, name="column.store"),
]
