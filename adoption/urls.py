from django.urls import path
from .views import home  # ← เชื่อมกับ views.py ที่แก้ไขแล้ว!

urlpatterns = [
    path('', home, name='home'),
]
