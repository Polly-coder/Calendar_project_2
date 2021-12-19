# Generated by Django 4.0 on 2021-12-18 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0003_remove_event_place_event_guest_alter_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Start')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetme.event', verbose_name='Event')),
            ],
        ),
    ]
