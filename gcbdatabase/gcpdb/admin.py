from django.contrib import admin
from .models import Gcpdb, Refseq, RefseqGcpdb , Pmid, GeneSymbol, Uniprot, UniprotGcpdb

admin.site.register(Uniprot)
admin.site.register(UniprotGcpdb)
admin.site.register(Gcpdb)
admin.site.register(Refseq)
admin.site.register(RefseqGcpdb)
admin.site.register(Pmid)
admin.site.register(GeneSymbol)









