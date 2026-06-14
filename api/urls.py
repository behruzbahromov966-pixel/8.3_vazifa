from django.urls import path

from .views import ConstructionCompanyApiView, CommentApiView, BuildingApiView

urlpatterns = [
    path("companies/", ConstructionCompanyApiView.as_view()),
    path("companies/<int:pk>/", ConstructionCompanyApiView.as_view()),
    path("buildings/", BuildingApiView.as_view()),
    path("buildings/<int:pk>/", BuildingApiView.as_view()),
    path("comments/", CommentApiView.as_view()),
    path("comments/<int:pk>/", CommentApiView.as_view()),
]