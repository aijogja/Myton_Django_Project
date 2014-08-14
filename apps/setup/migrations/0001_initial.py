# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostageCountry'
        db.create_table(u'setup_postagecountry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
            ('band', self.gf('django.db.models.fields.CharField')(default='1', max_length=10, null=True)),
            ('vat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'setup', ['PostageCountry'])

        # Adding model 'PostageRate'
        db.create_table(u'setup_postagerate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('band', self.gf('django.db.models.fields.CharField')(default='1', max_length=10, null=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('nextday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight_start', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight_to', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=18, decimal_places=2)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'setup', ['PostageRate'])


    def backwards(self, orm):
        # Deleting model 'PostageCountry'
        db.delete_table(u'setup_postagecountry')

        # Deleting model 'PostageRate'
        db.delete_table(u'setup_postagerate')


    models = {
        u'setup.postagecountry': {
            'Meta': {'object_name': 'PostageCountry'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'band': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '10', 'null': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vat': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'setup.postagerate': {
            'Meta': {'object_name': 'PostageRate'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'band': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '10', 'null': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nextday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'weight_start': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_to': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['setup']