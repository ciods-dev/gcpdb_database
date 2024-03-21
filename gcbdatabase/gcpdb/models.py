from django.db import models

class Pmid(models.Model):
    pmid = models.IntegerField(unique = True, primary_key = True)
    year = models.CharField(max_length = 50, null = True, blank = True)
    country = models.CharField(max_length = 50, null = True, blank = True)

    marker = models.ManyToManyField('Marker', 
                        through="PmidMarker", 
                        related_name="pmid_marker")
    
    def __str__(self):
        return str(self.pmid)

class Marker(models.Model):
    type_of_marker = models.CharField(max_length = 255,unique = True, primary_key = True)


    def __str__(self):
        return str(self.type_of_marker)

class Gcpdb(models.Model):
    sample_type	= models.CharField(max_length = 100, null = True, blank = True)
    stomach_tissue_type = models.CharField(max_length = 100, null = True, blank = True)
    part_of_stomach = models.CharField(max_length = 100, null = True, blank = True)
    no_of_patients = models.CharField(max_length = 100, null = True, blank = True)
    cohorts = models.CharField(max_length = 100, null = True, blank = True)
    validation_method = models.CharField(max_length = 100, null = True, blank = True)
    validation_sample_size = models.CharField(max_length = 100, null = True, blank = True)
    control	= models.CharField(max_length = 100, null = True, blank = True)
    fold_change = models.CharField(max_length = 100, null = True, blank = True)
    over_expression = models.CharField(max_length = 10, null = True, blank = True)
    down_expression = models.CharField(max_length = 10, null = True, blank = True)
    subtype_of_cancer = models.CharField(max_length = 100, null = True, blank = True)
    cancer_grade = models.CharField(max_length = 100, null = True, blank = True)
    stage = models.CharField(max_length = 100, null = True, blank = True)
    treatment_given	= models.CharField(max_length = 100, null = True, blank = True)
    chemotherapy_drug_regimen = models.CharField(max_length = 100, null = True, blank = True)
    mass_spec_platforms = models.CharField(max_length = 50, null = True, blank = True)  
    mass_spec_acquisition = models.CharField(max_length = 50, null = True, blank = True)  
    search_engine = models.CharField(max_length = 50, null = True, blank = True)
    bacterial_viral_infection = models.CharField(max_length = 50, null = True, blank = True)
    remarks = models.CharField(max_length = 50, null = True, blank = True) 
    remark_on_expression = models.CharField(max_length = 50, null = True, blank = True) 

    pmid = models.ManyToManyField('Pmid', 
                        through="PmidGcpdb", 
                        related_name="pmid_gcpdb")

    gene_symbol = models.ManyToManyField('GeneSymbol', 
                        through="GenesymbolGcpdb", 
                        related_name="genesymbol_gcpdb")
 
    uniprot = models.ManyToManyField('Uniprot', 
                        through="UniprotGcpdb", 
                        related_name="uniprot_gcpdb")
    
     
    refseq = models.ManyToManyField('Refseq', 
                        through="RefseqGcpdb", 
                        related_name="refseq_gcpdb")


class GeneSymbol(models.Model):
    gene_symbol = models.CharField(max_length = 100, unique = True, primary_key = True)

    def __str__(self):
        return self.gene_symbol

class Refseq(models.Model):
    refseq = models.CharField(max_length = 100, unique = True, primary_key = True)

    gene_symbol = models.ForeignKey(
        GeneSymbol, on_delete=models.PROTECT, related_name="refseq_genesymbol"
    )

    def __str__(self):
        return self.refseq
    

class Uniprot(models.Model):
    uniprot_id = models.CharField(max_length = 100, unique = True, primary_key = True)

    gene_symbol = models.ForeignKey(
        GeneSymbol, on_delete=models.PROTECT, related_name="uniprot_genesymbol"
    )

    def __str__(self):
        return self.uniprot_id



#========================Connecting tables for Many to many relations==========================================

class RefseqGcpdb(models.Model):

    refseq = models.ForeignKey(
        Refseq, on_delete=models.CASCADE, related_name="refseq_gcpdb_ref"
    )
    gcpdb = models.ForeignKey(
        Gcpdb, on_delete=models.CASCADE, related_name="refseq_gcpdb_gcpdb"
    )

    class Meta:
        unique_together = ("refseq","gcpdb")
 


class UniprotGcpdb(models.Model):

    uniprot = models.ForeignKey(
        Uniprot, on_delete=models.CASCADE, related_name="uniprot_gcpdb_uni"
    )
    gcpdb = models.ForeignKey(
        Gcpdb, on_delete=models.CASCADE, related_name="uniprot_gcpdb_uni_gcpdb"
    )

    class Meta:
        unique_together = ("uniprot","gcpdb")
 


class GenesymbolGcpdb(models.Model):

    gene_symbol = models.ForeignKey(
        GeneSymbol, on_delete=models.CASCADE, related_name="genesymbol_gcpdb_gs"
    )
    gcpdb = models.ForeignKey(
        Gcpdb, on_delete=models.CASCADE, related_name="genesymbol_gcpdb_gcpdb"
    )

    class Meta:
        unique_together = ("gene_symbol","gcpdb")


class PmidGcpdb(models.Model):

    pmid = models.ForeignKey(
        Pmid, on_delete=models.CASCADE, related_name="Pmid_gcpdb_pm"
    )
    gcpdb = models.ForeignKey(
        Gcpdb, on_delete=models.CASCADE, related_name="Pmid_gcpdb_gc"
    )

    class Meta:
        unique_together = ("pmid","gcpdb")



class PmidMarker(models.Model):

    pmid = models.ForeignKey(
        Pmid, on_delete=models.CASCADE, related_name="pmid_marker_pm"
    )
    type_of_marker = models.ForeignKey(
        Marker, on_delete=models.CASCADE, related_name="pmid_marker_tm"
    )

    class Meta:
        unique_together = ("pmid","type_of_marker")