# Generated by Django 4.2.6 on 2023-10-15 15:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_generatedprime'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedprime',
            name='prime_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
