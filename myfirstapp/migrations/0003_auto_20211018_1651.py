# Generated by Django 3.2.8 on 2021-10-18 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0002_alter_dog_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('house', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='pr5_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=50)),
                ('student_year', models.CharField(choices=[('F', 'Freshman'), ('S', 'Sophomore'), ('J', 'Junior'), ('S', 'Senior')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='dog',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Dog',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
