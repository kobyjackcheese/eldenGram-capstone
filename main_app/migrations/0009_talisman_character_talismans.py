# Generated by Django 4.2.3 on 2023-07-12 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_character_dexstat_character_endstat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talisman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='character',
            name='talismans',
            field=models.ManyToManyField(to='main_app.talisman'),
        ),
    ]
