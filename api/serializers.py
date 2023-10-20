from rest_framework import serializers
from .models import NewsletterSubscription, Contact, Portfolio, PortfolioImage

class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'description', 'include_user_email']


class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ('image',)

class PortfolioSerializer(serializers.ModelSerializer):
    images = PortfolioImageSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'