# Generated by Django 2.2.2 on 2022-09-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220928_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='status_code',
            field=models.CharField(blank=True, default='5', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='urls',
            name='update_interval',
            field=models.CharField(blank=True, choices=[('5', 'Every 5 min'), ('10', 'Every 10 min'), ('15', 'Every 15 min')], default=5, max_length=10, null=True),
        ),
    ]