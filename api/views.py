from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Header, FeedbackPost, Product, Services, Feedback, StaticText, Main, HoweWork
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
        user_agreement_url = None
        if footer_instances:
            first_footer_instance = footer_instances[0]
            if first_footer_instance.user_agreement:
                user_agreement_url = request.build_absolute_uri(first_footer_instance.user_agreement.url)

        print(user_agreement_url)

        # Добавляем поле user_agreement внутри объекта footer
        print(user_agreement_url)
        combined_footer_data = []
        for footer_data in footer_serializer.data:
            footer_data['user_agreement'] = user_agreement_url
            combined_footer_data.append(footer_data)
        # Получаем полную URL до файла user_agreement

        combined_data = {
            'headers': header_serializer.data,
            'footers': footer_serializer.data,
        }

        return Response(combined_data)


class CombinedDataView(APIView):
    def get(self, request):
        active_static_texts = StaticText.objects.filter(Is_Active=True)
        main = Main.objects.all()
        howework = HoweWork.objects.all()
        products = Product.objects.all()
        services = Services.objects.all()
        feedback = Feedback.objects.all()

        serializer = CombinedDataSerializer({
            'main': main,
            'howework': howework,
            'static': active_static_texts,
            'products': products,
            'services': services,
            'feedback': feedback,
        })

        return Response(serializer.data)


class FeedbackPostCreateView(generics.CreateAPIView):
    queryset = FeedbackPost.objects.all()
    serializer_class = FeedbackPostSerializer
