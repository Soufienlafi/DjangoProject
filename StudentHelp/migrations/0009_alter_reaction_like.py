# Generated by Django 5.0.4 on 2024-05-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentHelp', '0008_remove_post_likes_alter_reaction_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
