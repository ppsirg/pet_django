# Generated by Django 2.0.3 on 2018-05-03 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=20)),
            ],
        ),
    ]