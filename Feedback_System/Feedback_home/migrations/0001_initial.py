# Generated by Django 2.2.3 on 2019-09-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('Id_Number', models.IntegerField(primary_key=True, serialize=False)),
                ('Faculty_Name', models.CharField(max_length=100)),
                ('Email_Id', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
