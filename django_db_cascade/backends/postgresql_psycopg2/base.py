from django.db.backends.postgresql.base import DatabaseWrapper as DBW
from django_db_cascade.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor

class DatabaseWrapper(DBW):
    SchemaEditorClass = DatabaseSchemaEditor

