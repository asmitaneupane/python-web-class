# Generated by Django 2.1.7 on 2019-04-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190402_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]