# Generated by Django 5.0.4 on 2024-04-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentHelp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Stage', 'Stage'), ('Logement', 'Logement'), ('Transport', 'Transport'), ('Recommandation', 'Recommandation'), ('Evenement', 'Evenement')], max_length=50),
        ),
    ]
