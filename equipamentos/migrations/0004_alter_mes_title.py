# Generated by Django 4.1.7 on 2023-03-20 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0003_alter_mes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mes',
            name='title',
            field=models.TextField(),
        ),
    ]