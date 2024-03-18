from django.contrib import admin
from .models import Gcpdb, Refseq, RefseqGcpdb , Pmid


admin.site.register(Gcpdb)
admin.site.register(Refseq)
admin.site.register(RefseqGcpdb)
admin.site.register(Pmid)