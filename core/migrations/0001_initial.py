# Generated by Django 5.2.3 on 2025-07-18 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='core.pais')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('provincia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localidades', to='core.provincia')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('numero_documento', models.CharField(max_length=30, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.genero')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.localidad')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipodocumento')),
            ],
        ),
        migrations.AddConstraint(
            model_name='provincia',
            constraint=models.UniqueConstraint(fields=('pais', 'nombre'), name='unique_provincia_por_pais'),
        ),
        migrations.AddConstraint(
            model_name='localidad',
            constraint=models.UniqueConstraint(fields=('provincia', 'nombre'), name='unique_localidad_por_provincia'),
        ),
    ]
