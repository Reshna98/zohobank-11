# Generated by Django 4.2.2 on 2023-12-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0002_bankcreation_balance_alter_bankcreation_opn_bal'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='name',
            field=models.CharField(blank=True, default='', max_length=220, null=True),
        ),
    ]