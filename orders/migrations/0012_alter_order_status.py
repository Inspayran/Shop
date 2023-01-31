# Generated by Django 4.1.5 on 2023-01-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('New', 'New'), ('Cancelled', 'Cancelled')], default='New', max_length=10),
        ),
    ]