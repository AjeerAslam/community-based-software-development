from django.db import connections
from django.db import models
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
    md_status = models.CharField(max_length=100)

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
    pr_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'projects'
