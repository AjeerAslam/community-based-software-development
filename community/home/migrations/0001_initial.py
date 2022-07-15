# Generated by Django 4.0.6 on 2022-07-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('cl_id', models.AutoField(primary_key=True, serialize=False)),
                ('cl_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('cl_email', models.CharField(blank=True, max_length=1000, null=True)),
                ('cl_phone', models.IntegerField(blank=True, null=True)),
                ('cl_address', models.TextField(blank=True, null=True)),
                ('cl_password', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consists',
            fields=[
                ('cn_pr_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cn_md_id', models.IntegerField()),
                ('cn_md_due', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'consists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('dev_id', models.AutoField(primary_key=True, serialize=False)),
                ('dev_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('dev_email', models.CharField(blank=True, max_length=1000, null=True)),
                ('dev_phone', models.IntegerField(blank=True, null=True)),
                ('dev_address', models.TextField(blank=True, null=True)),
                ('dev_password', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'developers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experts',
            fields=[
                ('ex_id', models.AutoField(primary_key=True, serialize=False)),
                ('ex_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('ex_email', models.CharField(blank=True, max_length=1000, null=True)),
                ('ex_phone', models.IntegerField(blank=True, null=True)),
                ('ex_address', models.TextField(blank=True, null=True)),
                ('ex_password', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'experts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('fl_id', models.AutoField(primary_key=True, serialize=False)),
                ('fl_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('fl_description', models.TextField(blank=True, null=True)),
                ('fl_file', models.TextField(blank=True, null=True)),
                ('fl_md_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('md_id', models.AutoField(primary_key=True, serialize=False)),
                ('md_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('md_input', models.TextField(blank=True, null=True)),
                ('md_input_file', models.TextField(blank=True, null=True)),
                ('md_description', models.TextField(blank=True, null=True)),
                ('md_output', models.TextField(blank=True, null=True)),
                ('md_output_file', models.TextField(blank=True, null=True)),
                ('md_dev_id', models.IntegerField(blank=True, null=True)),
                ('md_status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'modules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('pr_id', models.AutoField(primary_key=True, serialize=False)),
                ('pr_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('pr_type', models.CharField(blank=True, max_length=1000, null=True)),
                ('pr_description', models.TextField(blank=True, null=True)),
                ('pr_due', models.DateTimeField(blank=True, null=True)),
                ('pr_closing', models.TextField(blank=True, null=True)),
                ('pr_file', models.TextField(blank=True, null=True)),
                ('pr_cl_id', models.IntegerField(blank=True, null=True)),
                ('pr_ex_id', models.IntegerField(blank=True, null=True)),
                ('pr_status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'projects',
                'managed': False,
            },
        ),
    ]
