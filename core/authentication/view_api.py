# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from .forms import FileUploadForm
from .tasks import process_csv_file
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer

class RegisterCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []


class LoginAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []


class UploadFile(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get(self, request):
        """
        Handle GET request (returns form data as a response in JSON).
        """
        # No need for the form in a typical API, but you can return a simple message
        return Response({"message": "Welcome to the home API, authenticated user!"})

    def post(self, request):
        """
        Handle POST request to upload a file and process it.
        """
        if 'file' not in request.FILES:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        # Get the absolute file path
        file_path = fs.path(filename)

        # Call the Celery task to process the file in the background
        process_csv_file.delay(file_path, request.user.id)

        # Return success response
        return Response({
            "message": "File uploaded successfully! Processing in the background.",
            "file_url": file_url
        }, status=status.HTTP_201_CREATED)
