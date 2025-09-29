from django.urls import path, include

from organizedata import views 







urlpatterns = [
    path('', views.landing_page)
]