from django.urls import path

from app.careers.views import CareerAPIView

urlpatterns = [
    path('', CareerAPIView.as_view(), ),
    path('<int:career_id>/', CareerAPIView.as_view(), ),
]
