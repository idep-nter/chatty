# Generated by Django 3.2.16 on 2023-01-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='registration_date',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
