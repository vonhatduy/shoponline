# Generated by Django 2.0.6 on 2018-09-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]
