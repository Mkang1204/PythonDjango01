from django.db import models
from django.utils import timezone

class Run(models.Model):
    '''A Next geenration sequncing run from NGS core'''
    id = models.IntegerField(primary_key = True)
    # user = models.CharField(max_length=50)
    runDate = models.DateTimeField(blank=True, null = True)
    FlowCell_ID = models.CharField(max_length = 10)
    ReagentsCartridge_Cycles = models.IntegerField
    ReagentsCartridge_Lot = models.CharField()
    BufferCartridge_Lot = models.CharField()
    Read_1 = models.IntegerField
    Read_2 = models.IntegerField
    Index_1 = models.IntegerField
    Index_2 = models.IntegerField
    RunName = models.CharField(max_length=100,   blank=True, null = True)
    ExportFolderName = models.CharField(max_length=100,   blank=True, null = True)
    PI = models.CharField(max_length=100, null=True)
    Investigator = models.CharField(max_length=50)
    ExperimentName = models.CharField(max_length=100)
    Reads = models.CharField(max_length=10)
    Assays = models.CharField(max_length=10)
    Protocol = models.CharField(max_length=10)
    ClusterDensity = models.CharField(max_length=10)
    Comments = models.CharField(max_length=300)
    Pool_id = models.ForeignKey(Pool, on_delete = models.CASCADE)

class Sample(models.Model):
    '''the sample describes the info about the sample before the library and RNAseq'''
    id = models.IntegerField(primary_key = True)
    # user = models.CharField(max_length=50)
    collectionDate = models.DateTimeField(blank=True, null = True)
    name = models.CharField(max_length=100, blank=True, null = True)
    organism = models.CharField(max_length=20, null=True)

class User(models.Model):
    '''tells us who is related to the experiment or 
    submitted the sequncing run'''

class LibraryIndex(models.Model):
    '''from sample to the corresponding library'''
class LibraryPrep(models.Model):



