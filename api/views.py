from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Header, FeedbackPost, Product, Services, Feedback, StaticText
from .serializers import HeaderSerializers, FooterSerializers, FeedbackSerializer, FeedbackPostSerializer, \
    CombinedDataSerializer

from rest_framework.generics import ListAPIView


# Create your views here.
class CombinedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        header_instances = Header.objects.all()
        footer_instances = Header.objects.all()

        header_serializer = HeaderSerializers(header_instances, many=True)
        footer_serializer = FooterSerializers(footer_instances, many=True)

        combined_data = {
            'headers': header_serializer.data,
            'footers': footer_serializer.data
        }

        return Response(combined_data)


class CombinedDataView(APIView):
    def get(self, request):
        active_static_texts = StaticText.objects.filter(Is_Active=True)
        products = Product.objects.all()
        services = Services.objects.all()
        feedback = Feedback.objects.all()

        serializer = CombinedDataSerializer({
            'static': active_static_texts,
            'products': products,
            'services': services,
            'feedback': feedback,
        })

        return Response(serializer.data)


class FeedbackPostCreateView(generics.CreateAPIView):
    queryset = FeedbackPost.objects.all()
    serializer_class = FeedbackPostSerializer
