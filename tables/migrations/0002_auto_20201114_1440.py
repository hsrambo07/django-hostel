# Generated by Django 3.0.8 on 2020-11-14 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='parent_name',
            field=models.ForeignKey(blank=True, db_column='parent_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Parent'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_room_no',
            field=models.ForeignKey(blank=True, db_column='s_room_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Room'),
        ),
    ]
