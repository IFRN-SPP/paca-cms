# Generated by Django 5.0 on 2025-02-12 02:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='cover',
            field=models.ImageField(blank=True, upload_to='issue/'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='document',
            field=models.FileField(blank=True, upload_to='issue/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'PDF'])]),
        ),
        migrations.AlterField(
            model_name='publication',
            name='logo',
            field=models.ImageField(blank=True, upload_to='publication/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='logo_mini',
            field=models.ImageField(blank=True, upload_to='publication/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='promo_image',
            field=models.ImageField(blank=True, upload_to='publication/'),
        ),
        migrations.CreateModel(
            name='BackgroundImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('image', models.ImageField(upload_to='background/')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.publication')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
