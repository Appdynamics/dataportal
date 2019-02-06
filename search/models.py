# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class dm_tasks(models.Model):
    script_file_name = models.CharField(max_length=1000, blank=True, null=True)
    script_type = models.CharField(max_length=1000, blank=True, null=True)
    config_file_name = models.CharField(max_length=1000, blank=True, null=True)
    query_file_name = models.CharField(max_length=1000, blank=True, null=True)
    af_priority_weight = models.IntegerField(blank=True, null=True)
    af_is_active = models.BooleanField(blank=True, null=True)
    af_intraday_is_active = models.BooleanField(blank=True, null=True)
    intraday_config_file_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dm_tasks'


class Entities(models.Model):
    name = models.CharField(max_length=1000)
    source_system = models.CharField(max_length=1000)
    fields_metadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)
    is_valid = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'entities'


class InfaTasks(models.Model):
    id = models.CharField(primary_key=True,max_length=1000)
    name = models.CharField(max_length=1000, blank=True, null=True)
    infa_post_processing_cmd = models.CharField(max_length=1000, blank=True, null=True)
    script_file_name = models.CharField(max_length=1000, blank=True, null=True)
    config_file_name = models.CharField(max_length=1000, blank=True, null=True)
    infa_file_name = models.CharField(max_length=1000, blank=True, null=True)
    af_priority_weight = models.IntegerField(blank=True, null=True)
    af_is_active = models.BooleanField(blank=True, null=True)
    org_id = models.CharField(max_length=1000, blank=True, null=True)
    server = models.CharField(max_length=1000, blank=True, null=True)
    af_intraday_is_active = models.BooleanField(blank=True, null=True)
    af_swat_is_active = models.BooleanField(blank=True, null=True)
    af_test_is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infa_tasks'
        unique_together = (('id', 'org_id', 'server'),)


class Integrations(models.Model):
    name = models.CharField(max_length=1000)
    entity_id = models.IntegerField()
    s3_entity = models.CharField(max_length=1000)
    integration_rules = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)
    is_valid = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'integrations'


class S3Files(models.Model):
    id = models.CharField(primary_key=True, max_length=1000)
    s3_path = models.CharField(max_length=1000)
    s3_bucket = models.CharField(max_length=1000)
    downloader = models.CharField(max_length=1000)
    downloader_instance = models.CharField(max_length=1000, blank=True, null=True)
    source_sys = models.CharField(max_length=1000)
    entity = models.CharField(max_length=1000)
    fields = models.TextField(blank=True, null=True)  # This field type is a guess.
    row_count = models.IntegerField(blank=True, null=True)
    uploaded_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 's3_files'
