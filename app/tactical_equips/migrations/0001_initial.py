# Generated by Django 2.1.1 on 2018-09-27 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DollEquip',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('codename', models.CharField(blank=True, max_length=30, null=True)),
                ('rank', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('company', models.CharField(blank=True, max_length=5, null=True)),
                ('exclusiveRate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('maxLevel', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('build_time', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DollEquipStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pow', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hit', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('dodge', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('armor', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('bullet', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('critical_percent', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('critical_harm_rate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('speed', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('night_view', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('armor_piercing', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_equip_status', to='tactical_equips.DollEquip')),
            ],
        ),
    ]