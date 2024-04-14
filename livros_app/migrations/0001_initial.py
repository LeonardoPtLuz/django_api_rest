# Generated by Django 5.0.4 on 2024-04-14 20:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id_livro', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('ano_lancamento', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('paginas', models.IntegerField()),
                ('editora', models.CharField(max_length=255)),
                ('criado_em', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
