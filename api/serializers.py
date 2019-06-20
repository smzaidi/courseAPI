from rest_framework import serializers

class CourseSerializer(serializers.Serializer):

    number = serializers.CharField(max_length=200)
