# Generated by Django 3.0.3 on 2020-02-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('department', models.CharField(choices=[(1, 'computer'), (2, 'maths'), (3, 'physics')], max_length=1)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
