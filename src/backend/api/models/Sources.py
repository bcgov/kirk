'''
Model used to define source data sets
'''
from __future__ import unicode_literals
from django.db import models
from .ReplicationJobs import ReplicationJobs


class SourceTypes(object):
    '''
    These are the source types that we are trying to

    '''
    FGDB = 'FGDB'
    ORASDE = 'OracleSDE'
    ORA = 'Oracle'
    SSSDE = 'SQLServerSDE'
    SS = 'SqlServer'
    CSV = 'CSV'
    SHP = 'SHP'
    # only implementing FGDB at the moment. When add support for different
    # source types will add to the defs below.
    sourceTypes = ((FGDB, 'File Geodatabase'), )


class Sources(models.Model):
    '''
    Sources
    ----------------
    jobid: foreign key
    sourceTable: source table
    sourceType: used for routing to different FMW's would contain parameters
                like:
                FGDB | SQLSERVERSDE | ORACLE | ORACLESDE | CSV
    sourceDBSchema: source schema
    sourceDBName: database service name for oracle / dbname
    sourceDBHost:
    sourceDBPort:
    sourceFilePath: directory to where data is stored on a file sys.


    '''
    # jobid = models.IntegerField()
    sourceid = models.AutoField(primary_key=True)
    jobid = models.ForeignKey(ReplicationJobs, on_delete=models.CASCADE,
                              related_name='sources', to_field='jobid',
                              null=True)
    # changed length to 161 because esri fgdb allow for that table name
    # length
    # http://desktop.arcgis.com/en/arcmap/latest/manage-data/administer-file-gdbs/file-geodatabase-size-and-name-limits.htm
    sourceTable = models.CharField(max_length=161, blank=False, null=False,
                                   help_text='Source Table Name')
    sourceTypeDefs = SourceTypes()
    sourceType = models.CharField(max_length=30, blank=False, null=False, \
                                  choices=sourceTypeDefs.sourceTypes,
                                  default=sourceTypeDefs.sourceTypes[0][0])
    sourceDBSchema = models.CharField(max_length=30, blank=True, null=True)
    sourceDBName = models.CharField(max_length=30, blank=True, null=True)
    sourceDBHost = models.CharField(max_length=30, blank=True, null=True)
    sourceDBPort = models.IntegerField(blank=True, null=True)
    sourceFilePath = models.CharField(max_length=200, blank=True, null=True)
    sourceProjection = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.sourceid)
