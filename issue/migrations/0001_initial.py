# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'MyModel'
        db.create_table('issue_mymodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True, null=True)),
        ))
        db.send_create_signal('issue', ['MyModel'])

    def backwards(self, orm):
        # Deleting model 'MyModel'
        db.delete_table('issue_mymodel')

    models = {
        'issue.mymodel': {
            'Meta': {'object_name': 'MyModel'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['issue']
