from django.urls import path
from .views import *

urlpatterns = [
    # path('', Gullar_list, name='gullar-list'),
    path('', GullarAPIView.as_view(), name='gullar-list'),
    path('detail/<int:pk>/', GullarDetailApi.as_view(), name='gullar-list'),

]