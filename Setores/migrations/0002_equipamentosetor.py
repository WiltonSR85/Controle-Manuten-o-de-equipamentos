# Generated by Django 5.1.7 on 2025-07-13 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipamentos', '0001_initial'),
        ('Setores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipamentoSetor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipamentos.equipamento')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Setores.setor')),
            ],
            options={
                'verbose_name': 'Equipamento no Setor',
                'verbose_name_plural': 'Equipamentos nos Setores',
                'unique_together': {('equipamento', 'setor')},
            },
        ),
    ]
