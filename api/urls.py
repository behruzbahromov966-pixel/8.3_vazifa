from django.urls import path

from .views import (ConstructionCompanyApiView, CommentApiView, BuildingApiView,
                    ConstructionCompanyDetailApiView, BuildingDetailApiView, CommentDetailApiView)

urlpatterns = [
    path("companies/", ConstructionCompanyApiView.as_view()),
    path("companies/<int:pk>/", ConstructionCompanyDetailApiView.as_view()),
    path("buildings/", BuildingApiView.as_view()),
    path("buildings/<int:pk>/", BuildingDetailApiView.as_view()),
    path("comments/", CommentApiView.as_view()),
    path("comments/<int:pk>/", CommentDetailApiView.as_view()),
    path('buildings/company/<int:company_id>/', BuildingApiView.as_view()),
]