# Generated by Django 4.2.3 on 2023-07-16 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_character_chestplate_character_gloves_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='WeaponType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapons', to='main_app.weapontype'),
        ),
    ]
