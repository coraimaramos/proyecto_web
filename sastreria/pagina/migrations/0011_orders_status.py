# Generated by Django 2.0.1 on 2018-05-03 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0010_auto_20180503_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default='SINPAGAR', max_length=20),
        ),
    ]