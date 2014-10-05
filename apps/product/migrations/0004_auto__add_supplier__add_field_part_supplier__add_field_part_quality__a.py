# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Supplier'
        db.create_table(u'product_supplier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'product', ['Supplier'])

        # Adding field 'Part.supplier'
        db.add_column(u'product_part', 'supplier',
                      self.gf('smart_selects.db_fields.ChainedForeignKey')(blank=True, related_name='part_supplier', null=True, to=orm['product.Supplier']),
                      keep_default=False)

        # Adding field 'Part.quality'
        db.add_column(u'product_part', 'quality',
                      self.gf('django.db.models.fields.CharField')(default='GEN', max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Part.height'
        db.add_column(u'product_part', 'height',
                      self.gf('django.db.models.fields.DecimalField')(default=1, null=True, max_digits=18, decimal_places=2),
                      keep_default=False)

        # Adding field 'Part.width'
        db.add_column(u'product_part', 'width',
                      self.gf('django.db.models.fields.DecimalField')(default=1, null=True, max_digits=18, decimal_places=2),
                      keep_default=False)

        # Adding field 'Part.length'
        db.add_column(u'product_part', 'length',
                      self.gf('django.db.models.fields.DecimalField')(default=1, null=True, max_digits=18, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Supplier'
        db.delete_table(u'product_supplier')

        # Deleting field 'Part.supplier'
        db.delete_column(u'product_part', 'supplier_id')

        # Deleting field 'Part.quality'
        db.delete_column(u'product_part', 'quality')

        # Deleting field 'Part.height'
        db.delete_column(u'product_part', 'height')

        # Deleting field 'Part.width'
        db.delete_column(u'product_part', 'width')

        # Deleting field 'Part.length'
        db.delete_column(u'product_part', 'length')


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
            'buy_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            'car': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'car_part'", 'null': 'True', 'to': u"orm['product.Car']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'category'", 'null': 'True', 'to': u"orm['product.Category']"}),
            'chassis_range': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'derivitive': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discount_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'discount_code'", 'null': 'True', 'to': u"orm['product.DiscountCode']"}),
            'height': ('django.db.models.fields.DecimalField', [], {'default': '1', 'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'default': '1', 'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            'model': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['product.Model']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'part_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'default': "'GEN'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            'supersessions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'supplier': ('smart_selects.db_fields.ChainedForeignKey', [], {'blank': 'True', 'related_name': "'part_supplier'", 'null': 'True', 'to': u"orm['product.Supplier']"}),
            'surcharge': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': '1', 'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            'width': ('django.db.models.fields.DecimalField', [], {'default': '1', 'null': 'True', 'max_digits': '18', 'decimal_places': '2'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'product.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['product']