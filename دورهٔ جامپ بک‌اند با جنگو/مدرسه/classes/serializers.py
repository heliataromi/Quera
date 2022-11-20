from rest_framework import serializers

from .models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):

	class Meta:
		model = Classroom
		fields = '__all__'

	def validate_capacity(self, value):
		if value < 5:
			error = 'Capacity should be greater than 5'
			raise serializers.ValidationError(error)

		return value

	def validate_area(self, value):
		if value < 0:
			error = 'Area should be positive'
			raise serializers.ValidationError(error)

		return value
