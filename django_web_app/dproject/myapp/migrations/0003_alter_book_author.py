# Generated by Django 5.1.3 on 2024-11-09 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_customuser_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default='Author', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='myapp.customuser'),
        ),
    ]
