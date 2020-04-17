# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blog',
            table='Blog',
        ),
        migrations.AlterModelTable(
            name='catagory',
            table='Catagory',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='Comment',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='Tag',
        ),
    ]
