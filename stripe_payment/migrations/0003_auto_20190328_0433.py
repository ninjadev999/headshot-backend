# Generated by Django 2.0.5 on 2019-03-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_payment', '0002_auto_20190327_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripepayment',
            name='amount',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
