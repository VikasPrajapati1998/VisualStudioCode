from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('members/', views.members, name="members"),
]

