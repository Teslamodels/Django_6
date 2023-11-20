from django.urls import path
from .views import Info, math

urlpatterns = [
    path('', Info.as_view(), name='Info'),
    path('internet/', math.as_view(), name='math'),
    
]