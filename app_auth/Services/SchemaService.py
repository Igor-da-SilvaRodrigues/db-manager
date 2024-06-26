from django.db import connection

class SchemaService:
    def get_tables(schema_name):
        cursor = connection.cursor()
        tables = []
        cursor.execute(
            f"SELECT TABLE_NAME, TABLE_ROWS, ENGINE, TABLE_COLLATION FROM information_schema.tables WHERE TABLE_SCHEMA = '{schema_name}'"
        )
        
        for row in cursor.fetchall():
            tables.append({
                "table_name": row[0],
                "table_rows": row[1],
                "engine": row[2],
                "collation": row[3]
            })
        
        return tables

    def detail(schema_name: str):
        """Returns the details of a schema, including it's tables.

        Args:
            schema_name (str): The name of the schema
        """
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT DEFAULT_CHARACTER_SET_NAME, DEFAULT_ENCRYPTION FROM information_schema.schemata WHERE SCHEMA_NAME = '{schema_name}';"
        )
        row = cursor.fetchone()

        tables = SchemaService.get_tables(schema_name)
        
        return({
            "schema_name": schema_name,
            "default_character_set":row[0],
            "default_encryption":row[1],
            "tables": tables
        })
