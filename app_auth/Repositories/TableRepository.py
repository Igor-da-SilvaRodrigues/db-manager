from django.db import connection


def tableColumn(schema, table, column):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COLUMN_DEFAULT,IS_NULLABLE,COLUMN_TYPE,CHARACTER_MAXIMUM_LENGTH,COLUMN_KEY,COLUMN_COMMENT,CONSTRAINT_NAME,INFORMATION_SCHEMA.KEY_COLUMN_USAGE.REFERENCED_TABLE_NAME,INFORMATION_SCHEMA.KEY_COLUMN_USAGE.REFERENCED_COLUMN_NAME FROM information_schema.columns LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE ON INFORMATION_SCHEMA.KEY_COLUMN_USAGE.TABLE_NAME = information_schema.columns.TABLE_NAME AND INFORMATION_SCHEMA.KEY_COLUMN_USAGE.COLUMN_NAME = information_schema.columns.COLUMN_NAME WHERE information_schema.columns.TABLE_SCHEMA = %s and information_schema.columns.TABLE_NAME = %s and information_schema.columns.COLUMN_NAME = %s LIMIT 1;",
        (schema, table, column))

    if (cursor.rowcount == 0):
        return False;

    return cursor.fetchall();


def tableColumns(schema, table):
    cursor = connection.cursor()
    cursor.execute(

        "SELECT COLUMN_NAME,IS_NULLABLE,COLUMN_TYPE,COLUMN_KEY FROM information_schema.columns WHERE information_schema.columns.TABLE_SCHEMA = %s and information_schema.columns.TABLE_NAME = %s;",

        (schema, table))

    if (cursor.rowcount == 0):
        return False;

    return cursor.fetchall();
