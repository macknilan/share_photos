# Generated by Django 4.2.10 on 2024-03-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=150, verbose_name='comment'),
        ),
    ]
