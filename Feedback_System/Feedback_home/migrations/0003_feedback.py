# Generated by Django 2.2.3 on 2019-09-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback_home', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('Feedback_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Sundaram', models.CharField(max_length=100)),
                ('Rejina', models.CharField(max_length=100)),
                ('Kiranmai', models.CharField(max_length=100)),
                ('Shilpa', models.CharField(max_length=100)),
                ('College_feedback_review', models.CharField(max_length=2000)),
            ],
        ),
    ]
