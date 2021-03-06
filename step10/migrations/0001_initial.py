# encoding: utf-8
from south.db import db
from south.v2 import SchemaMigration

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'QuestionType'
        db.create_table('step10_questiontype', (
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('step10', ['QuestionType'])

        # Adding model 'QuestionSet'
        db.create_table('step10_questionset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=128)),
        ))
        db.send_create_signal('step10', ['QuestionSet'])

        # Adding model 'Question'
        db.create_table('step10_question', (
            ('text', self.gf('django.db.models.fields.TextField')(max_length=128)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step10.QuestionType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step10.QuestionSet'])),
        ))
        db.send_create_signal('step10', ['Question'])

        # Adding model 'AnswerSet'
        db.create_table('step10_answerset', (
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('step10', ['AnswerSet'])

        # Adding model 'SavedAnswer'
        db.create_table('step10_savedanswer', (
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step10.Question'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step10.AnswerSet'])),
        ))
        db.send_create_signal('step10', ['SavedAnswer'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'QuestionType'
        db.delete_table('step10_questiontype')

        # Deleting model 'QuestionSet'
        db.delete_table('step10_questionset')

        # Deleting model 'Question'
        db.delete_table('step10_question')

        # Deleting model 'AnswerSet'
        db.delete_table('step10_answerset')

        # Deleting model 'SavedAnswer'
        db.delete_table('step10_savedanswer')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'step10.answerset': {
            'Meta': {'object_name': 'AnswerSet'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'step10.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['step10.QuestionSet']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['step10.QuestionType']"})
        },
        'step10.questionset': {
            'Meta': {'object_name': 'QuestionSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '128'})
        },
        'step10.questiontype': {
            'Meta': {'object_name': 'QuestionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'step10.savedanswer': {
            'Meta': {'object_name': 'SavedAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['step10.AnswerSet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['step10.Question']"})
        }
    }
    
    complete_apps = ['step10']
