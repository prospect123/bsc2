# Generated by Django 3.2 on 2021-05-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
