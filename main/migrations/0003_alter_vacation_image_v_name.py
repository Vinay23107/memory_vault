# Generated by Django 4.2.3 on 2024-04-04 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_vacation_name_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation_image',
            name='v_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vacation_name'),
        ),
    ]
