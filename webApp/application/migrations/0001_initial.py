# Generated by Django 3.2.9 on 2021-11-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('family', models.TextField()),
                ('birth_date', models.TextField()),
                ('tel', models.BigIntegerField()),
                ('address', models.TextField()),
                ('gender', models.BinaryField()),
            ],
        ),
    ]
