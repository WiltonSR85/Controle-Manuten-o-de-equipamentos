# Generated by Django 5.1.7 on 2025-07-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipamentos', '0001_initial'),
        ('Setores', '0002_equipamentosetor'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='setores',
            field=models.ManyToManyField(related_name='equipamentos', through='Setores.EquipamentoSetor', to='Setores.setor'),
        ),
    ]
