# Generated by Django 4.1.5 on 2023-01-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('New', 'New')], default='New', max_length=10),
        ),
    ]