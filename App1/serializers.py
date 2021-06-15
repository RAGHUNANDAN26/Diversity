
from rest_framework import serializers
from App1.models import Students

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ["id","name","score"]
