# Generated by Django 2.2.19 on 2023-10-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20231027_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ads.Fuel'),
            preserve_default=False,
        ),
    ]