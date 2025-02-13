# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'DebugLogRecord.settings_pickled'
        db.delete_column('debug_logging_debuglogrecord', 'settings_pickled')

        # Deleting field 'DebugLogRecord.cache_calls_pickled'
        db.delete_column('debug_logging_debuglogrecord', 'cache_calls_pickled')

        # Deleting field 'DebugLogRecord.sql_queries_pickled'
        db.delete_column('debug_logging_debuglogrecord', 'sql_queries_pickled')

        # Adding field 'DebugLogRecord.settings'
        db.add_column('debug_logging_debuglogrecord', 'settings', self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True), keep_default=False)

        # Adding field 'DebugLogRecord.sql_queries'
        db.add_column('debug_logging_debuglogrecord', 'sql_queries', self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True), keep_default=False)

        # Adding field 'DebugLogRecord.cache_calls'
        db.add_column('debug_logging_debuglogrecord', 'cache_calls', self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True), keep_default=False)

        # Changing field 'TestRun.end'
        db.alter_column('debug_logging_testrun', 'end', self.gf('django.db.models.fields.DateTimeField')(null=True))


    def backwards(self, orm):
        
        # Adding field 'DebugLogRecord.settings_pickled'
        db.add_column('debug_logging_debuglogrecord', 'settings_pickled', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'DebugLogRecord.cache_calls_pickled'
        db.add_column('debug_logging_debuglogrecord', 'cache_calls_pickled', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'DebugLogRecord.sql_queries_pickled'
        db.add_column('debug_logging_debuglogrecord', 'sql_queries_pickled', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Deleting field 'DebugLogRecord.settings'
        db.delete_column('debug_logging_debuglogrecord', 'settings')

        # Deleting field 'DebugLogRecord.sql_queries'
        db.delete_column('debug_logging_debuglogrecord', 'sql_queries')

        # Deleting field 'DebugLogRecord.cache_calls'
        db.delete_column('debug_logging_debuglogrecord', 'cache_calls')

        # User chose to not deal with backwards NULL issues for 'TestRun.end'
        raise RuntimeError("Cannot reverse this migration. 'TestRun.end' and its values cannot be restored.")


    models = {
        'debug_logging.debuglogrecord': {
            'Meta': {'object_name': 'DebugLogRecord'},
            'cache_calls': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'cache_deletes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cache_get_many': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cache_gets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cache_hits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cache_misses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cache_num_calls': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cache_sets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cache_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'settings': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'sql_num_queries': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sql_queries': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'sql_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'test_run': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['debug_logging.TestRun']"}),
            'timer_cputime': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'timer_ivcsw': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timer_stime': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'timer_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'timer_utime': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'timer_vcsw': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'debug_logging.testrun': {
            'Meta': {'object_name': 'TestRun'},
            'avg_cache_hits': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_cache_misses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_cpu_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_sql_queries': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_sql_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_sql_queries': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'total_cache_hits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_cache_misses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_cpu_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_sql_queries': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_sql_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['debug_logging']
