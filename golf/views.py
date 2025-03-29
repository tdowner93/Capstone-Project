import random
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return render(request, 'golf/home.html')

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

def recommend_club(distance, wind_speed, rain):
    clubs = {
        "Driver": range(200, 300),
        "3 Wood": range(180, 220),
        "5 Iron": range(150, 180),
        "7 Iron": range(130, 150),
        "9 Iron": range(100, 130),
        "Pitching Wedge": range(50, 100),
        "Putter": range(0, 50),
    }

    # Adjust distance based on wind and rain
    if wind_speed > 15:
        distance -= 10  # Reduce distance for strong wind
    if rain:
        distance -= 5  # Reduce distance in rain

    for club, dist_range in clubs.items():
        if distance in dist_range:
            return club
    return "Unknown Club"

# Example call
club = recommend_club(distance=160, wind_speed=10, rain=False)
print(f"Recommended Club: {club}")
