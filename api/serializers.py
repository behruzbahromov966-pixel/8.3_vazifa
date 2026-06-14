from rest_framework import serializers

from .models import ConstructionCompany, Building, Comment

class ConstructionCompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=13)
    address = serializers.CharField(max_length=255)

    def create(self, validated_data):
        company = ConstructionCompany.objects.create(**validated_data)
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class BuildingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=255)
    floors = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=12, decimal_places=2)

    def create(self, validated_data):
        building = Building.objects.create(**validated_data)
        return building

    def update(self, instance, validated_data):
        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.floors = validated_data.get('floors', instance.floors)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance



class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    building_id = serializers.IntegerField()
    user = serializers.CharField()
    text = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment

    def update(self, instance, validated_data):
        instance.building_id = validated_data.get('building_id', instance.building_id)
        instance.user = validated_data.get('user', instance.user)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
