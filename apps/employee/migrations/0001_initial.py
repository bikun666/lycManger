# Generated by Django 2.1.5 on 2019-06-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employeeNo', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(default='', max_length=16)),
                ('authority', models.IntegerField(default='0')),
            ],
            options={
                'verbose_name': '社員表',
                'verbose_name_plural': '社員表',
                'db_table': 'employee',
            },
        ),
    ]
