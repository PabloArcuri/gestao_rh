# Generated by Django 4.0.3 on 2022-03-24 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_alter_funcionario_empresa'),
        ('registro_hora_extra', '0004_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.funcionario'),
        ),
    ]
