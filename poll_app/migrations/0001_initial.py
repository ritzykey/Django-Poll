# Generated by Django 3.1.1 on 2020-10-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('example', models.TextField(null=True)),
                ('options', models.JSONField(default={}, null=True)),
            ],
        ),
    ]
