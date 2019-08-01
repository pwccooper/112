# Generated by Django 2.1 on 2019-07-21 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_series'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.AddField(
            model_name='series',
            name='director',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='genre',
            field=models.ForeignKey(default=2019, on_delete=django.db.models.deletion.CASCADE, to='movies.Genre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='in_stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='release_year',
            field=models.IntegerField(default=2019),
            preserve_default=False,
        ),
    ]
