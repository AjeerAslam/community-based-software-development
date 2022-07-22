# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clients(models.Model):
    cl_id = models.AutoField(primary_key=True)
    cl_name = models.CharField(max_length=1000, blank=True, null=True)
    cl_email = models.CharField(max_length=1000, blank=True, null=True)
    cl_phone = models.IntegerField(blank=True, null=True)
    cl_address = models.TextField(blank=True, null=True)
    cl_password = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Consists(models.Model):
    cn_pr_id = models.IntegerField(primary_key=True)
    cn_md_id = models.IntegerField()
    cn_md_due = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consists'
        unique_together = (('cn_pr_id', 'cn_md_id'),)


class Developers(models.Model):
    dev_id = models.AutoField(primary_key=True)
    dev_name = models.CharField(max_length=1000, blank=True, null=True)
    dev_email = models.CharField(max_length=1000, blank=True, null=True)
    dev_phone = models.IntegerField(blank=True, null=True)
    dev_address = models.TextField(blank=True, null=True)
    dev_password = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Experts(models.Model):
    ex_id = models.AutoField(primary_key=True)
    ex_name = models.CharField(max_length=1000, blank=True, null=True)
    ex_email = models.CharField(max_length=1000, blank=True, null=True)
    ex_phone = models.IntegerField(blank=True, null=True)
    ex_address = models.TextField(blank=True, null=True)
    ex_password = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experts'


class Files(models.Model):
    fl_id = models.AutoField(primary_key=True)
    fl_name = models.CharField(max_length=1000, blank=True, null=True)
    fl_description = models.TextField(blank=True, null=True)
    fl_file = models.TextField(blank=True, null=True)
    fl_md_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class Modules(models.Model):
    md_id = models.AutoField(primary_key=True)
    md_name = models.CharField(max_length=1000, blank=True, null=True)
    md_input = models.TextField(blank=True, null=True)
    md_input_file = models.TextField(blank=True, null=True)
    md_description = models.TextField(blank=True, null=True)
    md_output = models.TextField(blank=True, null=True)
    md_output_file = models.TextField(blank=True, null=True)
    md_dev_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules'


class Projects(models.Model):
    pr_id = models.AutoField(primary_key=True)
    pr_name = models.CharField(max_length=1000, blank=True, null=True)
    pr_type = models.CharField(max_length=1000, blank=True, null=True)
    pr_description = models.TextField(blank=True, null=True)
    pr_due = models.DateTimeField(blank=True, null=True)
    pr_closing = models.TextField(blank=True, null=True)
    pr_file = models.TextField(blank=True, null=True)
    pr_cl_id = models.IntegerField(blank=True, null=True)
    pr_ex_id = models.IntegerField(blank=True, null=True)
    pr_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projects'