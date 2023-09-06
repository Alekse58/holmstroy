from django.conf import settings
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView

from .models import Header, IconMain, SlideMain, FeedbackPost, Product, Services, Feedback, StaticText, HoweWork, Main, \
    AboutAs


class IconMainSerializers(serializers.ModelSerializer):
    class Meta:
        model = IconMain
        fields = ('id', 'header_logo')


class SlideMainSerializers(serializers.ModelSerializer):
    class Meta:
        model = SlideMain
        fields = ('id', 'title')


class HeaderSerializers(serializers.ModelSerializer):
    array_slides = SlideMainSerializers(source='main_slide', many=True)
    array_icon = IconMainSerializers(source='icon_slide', many=True)

    class Meta:
        model = Header
        fields = ('id', 'name', 'email', 'phone_number', 'array_slides', 'array_icon')


class FooterSerializers(serializers.ModelSerializer):
    array_icon = SlideMainSerializers(source='icon_slide', many=True)

    class Meta:
        model = Header
        fields = ('id', 'name', 'email', 'year', 'phone_number', 'array_icon', 'company_description', 'user_agreement')


class CombinedSerializer(serializers.Serializer):
    header = HeaderSerializers()
    footer = FooterSerializers()

    class Meta:
        fields = ('header', 'footer')


class FeedbackPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackPost
        fields = ['name', 'phone_number']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Feedback
        fields = '__all__'


class StaticTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticText
        fields = '__all__'


class HoweWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoweWork
        fields = '__all__'


class AboutAsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutAs
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Main
        fields = ['title', 'text', 'image']


class CombinedDataSerializer(serializers.Serializer):
    static = StaticTextSerializer(many=True)
    main = MainSerializer(many=True)
    howework = HoweWorkSerializer(many=True)
    products = ProductSerializer(many=True)
    services = ServicesSerializer(many=True)
    about = AboutAsSerializer(many=True)
    feedback = FeedbackSerializer(many=True)

