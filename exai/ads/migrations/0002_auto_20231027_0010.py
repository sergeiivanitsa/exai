# Generated by Django 2.2.19 on 2023-10-26 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='photos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Image'),
        ),
    ]
