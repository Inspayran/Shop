# Generated by Django 4.1.5 on 2023-01-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
