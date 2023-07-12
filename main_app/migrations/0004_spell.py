# Generated by Django 4.2.3 on 2023-07-11 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_spelltype_delete_spell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('img', models.CharField(max_length=500)),
                ('SpellType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spells', to='main_app.spelltype')),
            ],
        ),
    ]
