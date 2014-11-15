# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('zip_code', models.CharField(max_length=9, verbose_name='Zip Code')),
                ('neighborhood', models.CharField(default='center', max_length=100, verbose_name='Neighborhood')),
                ('street', models.CharField(help_text='street or avenue or alley or highway ... plus a name', max_length=100, verbose_name='Street')),
                ('number', models.IntegerField(default=1000, verbose_name='Number')),
                ('complement', models.TextField(null=True, verbose_name='Complement', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=b'200', verbose_name='Slug')),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('state', models.CharField(max_length=2, verbose_name='State', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
            ],
            options={
                'ordering': ('state', 'name'),
                'abstract': False,
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'state')]),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(verbose_name='City', to='django_br_addresses.City'),
            preserve_default=True,
        ),
    ]
