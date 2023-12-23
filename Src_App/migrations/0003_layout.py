# Generated by Django 4.1.7 on 2023-12-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0002_art_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Design and Layout', max_length=2000)),
                ('header_img', models.ImageField(upload_to='layout', verbose_name='Header Image')),
                ('gardens_img', models.ImageField(upload_to='layout', verbose_name='Gardens Link Image')),
                ('artwork_img', models.ImageField(upload_to='layout', verbose_name='Artwork Link Image')),
                ('brothers_img', models.ImageField(upload_to='layout', verbose_name='Brothers Link Image')),
                ('brothers_title', models.CharField(max_length=100, verbose_name="Brothers' Page Heading")),
                ('retreat_center_img', models.ImageField(upload_to='layout', verbose_name='Retreat Center Link Image')),
                ('retreat_center_title', models.CharField(max_length=100, verbose_name='Retreat Center Page Heading')),
                ('lady_heading', models.CharField(max_length=100, verbose_name='Lady of Mepkin Page Heading')),
                ('lady_img', models.ImageField(upload_to='layout', verbose_name='Lady of Mepkin Image')),
                ('lady_text', models.TextField(verbose_name='About Lady of Mepkin')),
                ('cemetry_heading', models.CharField(max_length=100, verbose_name="Lauren's Cemetry Heading")),
                ('cemetry_img', models.ImageField(upload_to='layout', verbose_name="Lauren's Cemetry Image")),
                ('cemetry_text', models.TextField(verbose_name="About Lauren's Cemetry")),
            ],
        ),
    ]
