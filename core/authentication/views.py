from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Optional, for authentication check
# Create your views here.
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .forms import FileUploadForm
from .models import Company

import csv
from .tasks import process_csv_file  # Import the Celery task
# from .tasks import process_csv_file  # Import the Celery task
from django.contrib import messages  # Import the messages framework


class HomeView(View):
    def get(self, request):
        # Check if user is authenticated and redirect accordingly
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if not authenticated
        form = FileUploadForm()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        # Handle the file upload
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)

            # Get the absolute file path
            file_path = fs.path(filename)

            # Call the Celery task to process the file in the background
            process_csv_file.delay(file_path, request.user.id)

            # Use Django messages framework to pass a success message
            messages.success(request, f'File uploaded successfully! The processing is happening in the background.')

            # Redirect back to the home page
            return redirect('home')

        return render(request, 'home.html', {'form': form})


class login(LoginView):
    template_name='login.html'
    success_url='/'

    def get_success_url(self):
        return reverse_lazy('home') 