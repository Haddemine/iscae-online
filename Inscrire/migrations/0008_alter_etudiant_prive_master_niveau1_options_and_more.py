# Generated by Django 4.0.6 on 2022-07-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inscrire', '0007_etudiant_prive_licence_niveau1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etudiant_prive_master_niveau1',
            options={'verbose_name': 'Master privé M1', 'verbose_name_plural': 'Master privé M1'},
        ),
        migrations.AlterModelOptions(
            name='etudiant_prive_master_niveau2',
            options={'verbose_name': 'Master privé M2', 'verbose_name_plural': 'Master privé M2'},
        ),
        migrations.AddField(
            model_name='orientation',
            name='niveau',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
