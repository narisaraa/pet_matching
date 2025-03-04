from django.shortcuts import render

def home(request):
    return render(request, 'adoption/home.html')  # ← ให้ Django แสดงหน้า home.html
