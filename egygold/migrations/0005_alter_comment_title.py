# Generated by Django 3.2 on 2021-05-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egygold', '0004_auto_20210512_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='العنوان'),
        ),
    ]