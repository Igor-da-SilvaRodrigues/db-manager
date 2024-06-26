from django.db import connection
import json;


def schemaTables(schema, columns_as_json=False):
    cursor = connection.cursor();

    cursor.execute(
        "SELECT distinct TABLE_NAME, COLUMN_NAME FROM information_schema.columns WHERE TABLE_SCHEMA = %s", [schema])
    table_columns = {};

    for row in cursor.fetchall():
        if row[0] not in table_columns:
            table_columns[row[0]] = [];
            table_columns[row[0]].append(row[1]);
            continue;

        table_columns[row[0]].append(row[1]);

    if columns_as_json:
        for table in table_columns:
            table_columns[table] = json.dumps(table_columns[table]);

    return table_columns;
