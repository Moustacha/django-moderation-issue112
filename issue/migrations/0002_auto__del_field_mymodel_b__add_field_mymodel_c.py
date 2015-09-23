# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting field 'MyModel.b'
        db.delete_column('issue_mymodel', 'b')

        # Adding field 'MyModel.c'
        db.add_column('issue_mymodel', 'c',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'MyModel.b'
        db.add_column('issue_mymodel', 'b',
                      self.gf('django.db.models.fields.CharField')(max_length=400, blank=True, null=True),
                      keep_default=False)

        # Deleting field 'MyModel.c'
        db.delete_column('issue_mymodel', 'c')

    models = {
        'issue.mymodel': {
            'Meta': {'object_name': 'MyModel'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'c': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['issue']
