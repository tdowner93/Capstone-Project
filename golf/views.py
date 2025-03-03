import random
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'golf_simulator/home.html')

def simulate_shot(request):
    if request.method == 'POST':
        club = request.POST.get('club')
        power = int(request.POST.get('power', 50))  # Default power is 50%
        
        # Basic shot distance calculation
        club_distances = {
            'Driver': 230,
            'Iron': 150,
            'Putter': 20
        }
        
        base_distance = club_distances.get(club, 100)
        variation = random.uniform(-0.1, 0.1)  # 10% variation
        shot_distance = base_distance * (power / 100) * (1 + variation)
        
        return JsonResponse({'distance': round(shot_distance, 2)})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
