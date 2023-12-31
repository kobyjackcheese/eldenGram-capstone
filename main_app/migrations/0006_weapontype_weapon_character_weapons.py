# Generated by Django 4.2.3 on 2023-07-12 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('img', models.CharField(max_length=500)),
                ('WeaponType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spells', to='main_app.weapontype')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='weapons',
            field=models.ManyToManyField(to='main_app.weapon'),
        ),
    ]
