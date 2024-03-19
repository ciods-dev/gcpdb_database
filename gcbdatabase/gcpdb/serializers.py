from rest_framework import serializers
from .models import Gcpdb

class GcpdbSerializers(serializers.ModelSerializer):

    class Meta:
        model = Gcpdb
        fields = "__all__"









