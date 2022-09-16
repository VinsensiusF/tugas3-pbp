# Generated by Django 4.1.1 on 2022-09-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('release_date', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]
