# Generated by Django 5.0.6 on 2024-05-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0006_alter_employee_gender_alter_manager_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='empimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
    ]