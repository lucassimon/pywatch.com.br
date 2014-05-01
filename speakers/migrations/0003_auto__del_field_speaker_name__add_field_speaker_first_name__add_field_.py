# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Speaker.name'
        db.delete_column(u'speakers_speaker', 'name')

        # Adding field 'Speaker.first_name'
        db.add_column(u'speakers_speaker', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Speaker.last_name'
        db.add_column(u'speakers_speaker', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Speaker.email'
        db.add_column(u'speakers_speaker', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', unique=True, max_length=75, db_index=True),
                      keep_default=False)


        # Changing field 'Speaker.slug'
        db.alter_column(u'speakers_speaker', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

    def backwards(self, orm):
        # Adding field 'Speaker.name'
        db.add_column(u'speakers_speaker', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Deleting field 'Speaker.first_name'
        db.delete_column(u'speakers_speaker', 'first_name')

        # Deleting field 'Speaker.last_name'
        db.delete_column(u'speakers_speaker', 'last_name')

        # Deleting field 'Speaker.email'
        db.delete_column(u'speakers_speaker', 'email')


        # Changing field 'Speaker.slug'
        db.alter_column(u'speakers_speaker', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True))

    models = {
        u'speakers.kindcontact': {
            'Meta': {'object_name': 'KindContact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['speakers.Speaker']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'speakers.speaker': {
            'Meta': {'ordering': "['created']", 'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['speakers']