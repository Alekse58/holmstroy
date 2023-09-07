from django.urls import path
from django.conf.urls.static import static
from holmstroy import settings
from .views import CombinedAPIView, FeedbackPostCreateView, CombinedDataView
from .shema import urlpatterns as spectacular_urls

urlpatterns = [
    path('pagedata/', CombinedAPIView.as_view(), name='combined-api-view'),
    path('main/', CombinedDataView.as_view(), name='pagedata'),
    path('create-feedback/', FeedbackPostCreateView.as_view(), name='create-feedback'),
]
urlpatterns += spectacular_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)