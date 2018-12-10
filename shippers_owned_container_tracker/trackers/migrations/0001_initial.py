# Generated by Django 2.0.9 on 2018-12-10 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(unique=True)),
                ('reference_number', models.TextField(max_length=11)),
                ('container_number', models.TextField(max_length=11)),
                ('move_type', models.TextField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('operator_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operators.Operator')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
