# Generated by Django 5.0.6 on 2024-05-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_employee_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teamleader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Employee Name')),
                ('employeeid', models.BigIntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('salary', models.FloatField()),
                ('performance', models.CharField(max_length=50, verbose_name='Emp Performance')),
                ('doj', models.DateField()),
                ('empimage', models.ImageField(upload_to='image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
    ]
