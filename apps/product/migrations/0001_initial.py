# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table(u'product_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'product', ['Car'])

        # Adding model 'Model'
        db.create_table(u'product_model', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('car', self.gf('django.db.models.fields.related.ForeignKey')(related_name='car', to=orm['product.Car'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'product', ['Model'])

        # Adding model 'Category'
        db.create_table(u'product_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parent_category', null=True, to=orm['product.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'product', ['Category'])

        # Adding model 'DiscountCode'
        db.create_table(u'product_discountcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5, null=True)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'product', ['DiscountCode'])

        # Adding model 'Part'
        db.create_table(u'product_part', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('supersessions', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('car', self.gf('django.db.models.fields.related.ForeignKey')(related_name='car_part', null=True, to=orm['product.Car'])),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='model', null=True, to=orm['product.Model'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='category', null=True, to=orm['product.Category'])),
            ('chassis_range', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('derivitive', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('discount_code', self.gf('django.db.models.fields.related.ForeignKey')(related_name='discount_code', null=True, to=orm['product.DiscountCode'])),
            ('retail_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('buy_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('surcharge', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'product', ['Part'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table(u'product_car')

        # Deleting model 'Model'
        db.delete_table(u'product_model')

        # Deleting model 'Category'
        db.delete_table(u'product_category')

        # Deleting model 'DiscountCode'
        db.delete_table(u'product_discountcode')

        # Deleting model 'Part'
        db.delete_table(u'product_part')


    models = {
        u'product.car': {
            'Meta': {'object_name': 'Car'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'product.category': {
            'Meta': {'object_name': 'Category'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_category'", 'null': 'True', 'to': u"orm['product.Category']"})
        },
        u'product.discountcode': {
            'Meta': {'object_name': 'DiscountCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'product.model': {
            'Meta': {'object_name': 'Model'},
            'car': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'car'", 'to': u"orm['product.Car']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'product.part': {
            'Meta': {'object_name': 'Part'},
            'buy_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'car': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'car_part'", 'null': 'True', 'to': u"orm['product.Car']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'null': 'True', 'to': u"orm['product.Category']"}),
            'chassis_range': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'derivitive': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discount_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'discount_code'", 'null': 'True', 'to': u"orm['product.DiscountCode']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'model'", 'null': 'True', 'to': u"orm['product.Model']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'supersessions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'surcharge': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['product']