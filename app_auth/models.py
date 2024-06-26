from django.db import models

# Create your models here.

# Modelo de usuário do schema 'mysql'. Managed está desativado para impedir qualquer mudança na estrutura dessa tabela
# MUITO CUIDADO AO FAZER MIGRAÇÕES, NÃO MODIFIQUE ESTA TABELA!
class User(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase. The composite primary key (Host, User) found, that is not supported. The first column is selected.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    reload_priv = models.CharField(db_column='Reload_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    shutdown_priv = models.CharField(db_column='Shutdown_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    process_priv = models.CharField(db_column='Process_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    file_priv = models.CharField(db_column='File_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    show_db_priv = models.CharField(db_column='Show_db_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    super_priv = models.CharField(db_column='Super_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    repl_slave_priv = models.CharField(db_column='Repl_slave_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    repl_client_priv = models.CharField(db_column='Repl_client_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_user_priv = models.CharField(db_column='Create_user_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_tablespace_priv = models.CharField(db_column='Create_tablespace_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    ssl_type = models.CharField(max_length=9, db_collation='utf8mb3_general_ci')
    ssl_cipher = models.TextField()
    x509_issuer = models.TextField()
    x509_subject = models.TextField()
    max_questions = models.PositiveIntegerField()
    max_updates = models.PositiveIntegerField()
    max_connections = models.PositiveIntegerField()
    max_user_connections = models.PositiveIntegerField()
    plugin = models.CharField(max_length=64)
    authentication_string = models.TextField(blank=True, null=True)
    password_expired = models.CharField(max_length=1, db_collation='utf8mb3_general_ci')
    password_last_changed = models.DateTimeField(blank=True, null=True)
    password_lifetime = models.PositiveSmallIntegerField(blank=True, null=True)
    account_locked = models.CharField(max_length=1, db_collation='utf8mb3_general_ci')
    create_role_priv = models.CharField(db_column='Create_role_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    drop_role_priv = models.CharField(db_column='Drop_role_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password_reuse_history = models.PositiveSmallIntegerField(db_column='Password_reuse_history', blank=True, null=True)  # Field name made lowercase.
    password_reuse_time = models.PositiveSmallIntegerField(db_column='Password_reuse_time', blank=True, null=True)  # Field name made lowercase.
    password_require_current = models.CharField(db_column='Password_require_current', max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    user_attributes = models.JSONField(db_column='User_attributes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('host', 'user'),)
        db_table_comment = 'Users and global privileges'
        app_label = 'app_auth'
        
    def save(self, *args, **kwargs):
        return self

