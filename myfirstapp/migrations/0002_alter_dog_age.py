# Generated by Django 3.2.8 on 2021-10-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
