# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table(u'speakers_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'speakers', ['Speaker'])

        # Adding model 'KindContact'
        db.create_table(u'speakers_kindcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['speakers.Speaker'])),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'speakers', ['KindContact'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table(u'speakers_speaker')

        # Deleting model 'KindContact'
        db.delete_table(u'speakers_kindcontact')


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
            'bio': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['speakers']