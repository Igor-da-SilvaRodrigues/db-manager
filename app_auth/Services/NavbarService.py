from django.shortcuts import render
from django.db import connection
from collections import defaultdict

class NavbarService:
    def mount():
        cursor = connection.cursor()
        formated_columns = {};
        columns = cursor.execute(
            "SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA NOT IN ('information_schema', 'performance_schema', 'sys', 'mysql')"
        )

        for column in cursor.fetchall():
            if column[0] not in formated_columns:
                formated_columns[column[0]] = {
                    "schema": column[0],
                    "tables": {
                        column[1]: [column[2]]
                    }
                }
                continue

            if column[1] not in formated_columns[column[0]]['tables']:
                formated_columns[column[0]]['tables'][column[1]] = []

            formated_columns[column[0]]['tables'][column[1]].append(column[2])

        return formated_columns
