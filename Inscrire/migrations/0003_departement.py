# Generated by Django 4.0.6 on 2022-07-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inscrire', '0002_filiere_licence_filiere_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('filiere', models.ManyToManyField(blank=True, related_name='filiere', to='Inscrire.filiere')),
            ],
            options={
                'verbose_name': 'Departement',
                'verbose_name_plural': 'Departements',
            },
        ),
    ]
