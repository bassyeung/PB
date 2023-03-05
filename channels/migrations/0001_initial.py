# Generated by Django 3.2.16 on 2023-02-17 06:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('icon', models.ImageField(blank=True, upload_to='photos/channels/%Y/%m/%d')),
                ('banner', models.ImageField(blank=True, upload_to='photos/channels/%Y/%m/%d')),
                ('video', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('IT', 'IT'), ('music', 'music'), ('games', 'games'), ('finance', 'finance'), ('style', 'style'), ('fashion', 'fashion'), ('food', 'food')], max_length=200)),
                ('status', models.CharField(max_length=1)),
                ('tag', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdetails.userdetail')),
            ],
        ),
    ]
