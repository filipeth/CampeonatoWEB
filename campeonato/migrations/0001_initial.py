# Generated by Django 2.1.7 on 2019-02-27 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, default='Um campeonato a ser disputado.')),
                ('num_grupos', models.IntegerField(blank=True, default=16)),
                ('num_times', models.IntegerField(blank=True, default=80)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campeonato.Campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds_t1', models.IntegerField(default=0)),
                ('rounds_t2', models.IntegerField(default=0)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campeonato.Campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('jogos', models.IntegerField(default=0)),
                ('pontos', models.IntegerField(default=0)),
                ('rounds_ganhos', models.IntegerField(default=0)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campeonato.Campeonato')),
            ],
        ),
        migrations.AddField(
            model_name='partida',
            name='ganhador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='time_ganhador', to='campeonato.Team'),
        ),
        migrations.AddField(
            model_name='partida',
            name='time1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='time1', to='campeonato.Team'),
        ),
        migrations.AddField(
            model_name='partida',
            name='time2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='time2', to='campeonato.Team'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='jogos',
            field=models.ManyToManyField(default=None, to='campeonato.Partida'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='times',
            field=models.ManyToManyField(default=None, to='campeonato.Team'),
        ),
    ]