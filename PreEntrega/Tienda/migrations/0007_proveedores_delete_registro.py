# Generated by Django 5.0.3 on 2024-04-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0006_rename_usuario_registro_fname_registro_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RazonSocial', models.CharField(max_length=30)),
                ('NomFant', models.CharField(max_length=30, null=True)),
                ('RUT', models.CharField(max_length=30)),
                ('GIRO', models.CharField(max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]