# Generated by Django 3.0.5 on 2020-05-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preguntas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativa_seleccionada',
            name='id_alternativa_seleccionada',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
