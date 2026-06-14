from django.db.models import Model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.request import Request
from rest_framework.generics import get_object_or_404

from .models import Building, ConstructionCompany, Comment
from .serializers import ConstructionCompanySerializer, BuildingSerializer, CommentSerializer

class ConstructionCompanyApiView(APIView):
    def get(self, request, pk: int=None):
        if not pk:
            companies = ConstructionCompany.objects.all()
            serializer = ConstructionCompanySerializer(companies, many=True)
        else:
            company = get_object_or_404(ConstructionCompany, pk=pk)
            serializer = ConstructionCompanySerializer(company)
        return Response(serializer.data)

    def post(self, request, pk: int=None):
        if not pk:
            serializer = ConstructionCompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"message": "Method POST not allowed "})

    def put(self, request, pk: int=None):
        company = get_object_or_404(ConstructionCompany, pk=pk)
        serializer = ConstructionCompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk: int=None):
        company = get_object_or_404(ConstructionCompany, pk=pk)
        company.delete()
        return Response({"message": "Successfully deleted"}, status=204)

class BuildingApiView(APIView):
    def get(self, request, pk: int=None):
        if not pk:
            buildings = Building.objects.all()
            serializer = BuildingSerializer(buildings, many=True)
        else:
            building = get_object_or_404(Building, pk=pk)
            serializer = BuildingSerializer(building)
        return Response(serializer.data)

    def post(self, request, pk: int=None):
        if not pk:
            serializer = BuildingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"message": "Method POST not allowed "})

    def put(self, request, pk: int=None):
        building = get_object_or_404(Building, pk=pk)
        serializer = BuildingSerializer(instance=building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk: int=None):
        building = get_object_or_404(Building, pk=pk)
        building.delete()
        return Response({"message": "Successfully deleted"}, status=204)

class CommentApiView(APIView):
    def get(self, request, pk: int=None):
        if not pk:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
        else:
            comment = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def post(self, request, pk: int=None):
        if not pk:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"message": "Method POST not allowed "})

    def put(self, request, pk: int=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk: int=None):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({"message": "Successfully deleted"}, status=204)