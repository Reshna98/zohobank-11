# Generated by Django 4.2.2 on 2023-12-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankcreation',
            name='balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='bankcreation',
            name='opn_bal',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
