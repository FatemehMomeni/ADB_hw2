# Generated by Django 3.2.9 on 2021-11-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_users_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.TextField(),
        ),
    ]
