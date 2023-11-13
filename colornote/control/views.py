from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        # Assuming you have a model to store drawings, adjust this part accordingly
        drawing_data = request.POST.get('drawing_data')
        # Process and save the drawing_data as needed
        return JsonResponse({'status': 'success'})

    return render(request, 'home_3.html')
