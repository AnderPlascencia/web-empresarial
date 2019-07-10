from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:slug_page>/', views.page, name="pages"),
]