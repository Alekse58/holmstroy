from django.urls import path
from .views import CombinedAPIView, FeedbackPostCreateView, CombinedDataView

urlpatterns = [
    path('pagedata/', CombinedAPIView.as_view(), name='combined-api-view'),
    path('main/', CombinedDataView.as_view(), name='pagedata'),

    path('create-feedback/', FeedbackPostCreateView.as_view(), name='create-feedback'),

]