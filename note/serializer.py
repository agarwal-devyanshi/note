# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import NotesModel

# Create a model serializer
class NotesSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = NotesModel
		# fields = ('title', 'description')
