# Generated by Django 4.1.7 on 2023-03-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0002_alter_mes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mes',
            name='title',
            field=models.CharField(choices=[['u', 'J'], ['a', 'J'], ['g', 'A'], ['u', 'J'], ['e', 'S'], ['o', 'N'], ['e', 'D'], ['u', 'O'], ['b', 'A'], ['a', 'M'], ['e', 'F'], ['a', 'M']], default='Janeiro', max_length=1000),
        ),
    ]