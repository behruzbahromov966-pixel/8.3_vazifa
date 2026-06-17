from django.db.models import Model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Building, ConstructionCompany, Comment
from .serializers import ConstructionCompanySerializer, BuildingSerializer, CommentSerializer

class ConstructionCompanyApiView(ListCreateAPIView):
    queryset = ConstructionCompany.objects.all()
    serializer_class = ConstructionCompanySerializer

class ConstructionCompanyDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = ConstructionCompany.objects.all()
    serializer_class = ConstructionCompanySerializer

class BuildingApiView(ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'company_id'

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")

        price = self.request.query_params.get('price')
        price_response =True if price == "high" else False if price == "low" else None

        if company_id:
            queryset = self.queryset.filter(company_id=company_id)
        else:
            queryset = self.queryset.all()

        if price_response == False:
            queryset = queryset.order_by('price')
        elif price_response == True:
            queryset = queryset.order_by('-price')
        else:
            pass
        return queryset


class BuildingDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class CommentApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer