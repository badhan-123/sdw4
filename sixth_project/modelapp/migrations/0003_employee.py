# Generated by Django 5.1.4 on 2025-01-02 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0002_student_father_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_field', models.DateTimeField(null=True)),
                ('url_field', models.URLField(null=True)),
                ('boolean_field', models.BooleanField(null=True)),
                ('foreign_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapp.employee')),
            ],
        ),
    ]
