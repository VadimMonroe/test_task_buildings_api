from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import BuildingsBase
import datetime


class BuildingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = BuildingsBase
		fields = '__all__'
		validators = [
			UniqueTogetherValidator(
				queryset=BuildingsBase.objects.all(),
				fields=['year', 'area']
			)
		]

	def validate(self, data):
		if data.get('year') < datetime.datetime.now().year - 5:
			raise serializers.ValidationError('No!')
		else:
			return data
