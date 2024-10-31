# Generated by Django 5.1.2 on 2024-10-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomCat', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dificultades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomDif', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='NomIng',
            field=models.CharField(max_length=40),
        ),
    ]
