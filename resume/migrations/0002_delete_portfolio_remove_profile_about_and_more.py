# Generated by Django 4.2.3 on 2023-07-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='category',
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='home',
            name='picture',
            field=models.ImageField(upload_to='picture/'),
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
