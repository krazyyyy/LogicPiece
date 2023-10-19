from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NewsletterSubscription, Contact
from .serializers import NewsletterSubscriptionSerializer, ContactSerializer

@api_view(['POST'])
def subscribe(request):
    serializer = NewsletterSubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        contact_instance = serializer.save()

        # Save the user's email to the newsletter if requested
        if serializer.validated_data.get('include_user_email'):
            newsletter_serializer = NewsletterSubscriptionSerializer(data={'email': serializer.validated_data['email']})
            if newsletter_serializer.is_valid():
                newsletter_serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)