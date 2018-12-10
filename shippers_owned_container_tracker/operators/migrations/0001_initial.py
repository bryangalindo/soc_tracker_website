# Generated by Django 2.0.9 on 2018-12-10 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(max_length=50)),
                ('type', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
