# Generated by Django 4.0.5 on 2022-06-19 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0004_alter_neighborhood_health_centers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='hoodapp.profile'),
        ),
    ]