from rest_framework import serializers

from .models import ConstructionCompany, Building, Comment

class ConstructionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionCompany
        fields = "__all__"


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"
        depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        depth = 1