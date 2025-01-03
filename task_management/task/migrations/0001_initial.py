# Generated by Django 5.1.4 on 2025-01-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('taskAssignDate', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(blank=True, to='category.taskcategory')),
            ],
        ),
    ]
