# Generated by Django 4.2.6 on 2023-10-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('carga_horaria', models.IntegerField()),
                ('data_criacao', models.DateTimeField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
