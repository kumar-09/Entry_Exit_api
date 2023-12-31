# Generated by Django 4.2.6 on 2023-10-15 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('email_id', models.CharField(max_length=120)),
                ('pswd', models.CharField(max_length=30)),
                ('phone_num', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='event_db',
            name='event_id',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='userid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.guests'),
        ),
        migrations.DeleteModel(
            name='guest',
        ),
    ]
