from rest_framework import serializers
from .models import *


class ClueSerializer(serializers.Serializer):
    uploaded_files = serializers.ListSerializer(
        child=serializers.FileField(allow_empty_file=False, use_url=False)
    )
