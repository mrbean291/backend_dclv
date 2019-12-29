# Generated by Django 2.2.5 on 2019-12-15 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common_models', '0001_initial'),
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='apartment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment_type', to='common_models.ApartmentType', to_field='type'),
        ),
    ]