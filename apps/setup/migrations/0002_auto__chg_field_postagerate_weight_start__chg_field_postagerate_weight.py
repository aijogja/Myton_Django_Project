# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PostageRate.weight_start'
        db.alter_column(u'setup_postagerate', 'weight_start', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits='50', decimal_places=2))

        # Changing field 'PostageRate.weight_to'
        db.alter_column(u'setup_postagerate', 'weight_to', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits='50', decimal_places=2))

    def backwards(self, orm):

        # Changing field 'PostageRate.weight_start'
        db.alter_column(u'setup_postagerate', 'weight_start', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'PostageRate.weight_to'
        db.alter_column(u'setup_postagerate', 'weight_to', self.gf('django.db.models.fields.FloatField')(null=True))

    models = {
        u'setup.postagecountry': {
            'Meta': {'object_name': 'PostageCountry'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'band': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '10', 'null': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True'}),
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
            'weight_start': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': "'50'", 'decimal_places': '2'}),
            'weight_to': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': "'50'", 'decimal_places': '2'})
        }
    }

    complete_apps = ['setup']