from django.shortcuts import render
import random
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'golf/home.html')  # optional homepage

def get_environment_factor(weather, slope, lie):
    factor = 1.0
    if weather == 'windy':
        factor -= 0.05
    elif weather == 'rainy':
        factor -= 0.10

    if slope == 'uphill':
        factor -= 0.10
    elif slope == 'downhill':
        factor += 0.10

    if lie == 'rough':
        factor -= 0.07
    elif lie == 'sand':
        factor -= 0.15

    return factor

def shot_predictor(request):
    if request.method == 'POST':
        name = request.POST['name']
        club = request.POST['club']
        distance = float(request.POST['distance'])
        weather = request.POST['weather']
        slope = request.POST['slope']
        lie = request.POST['lie']

        factor = get_environment_factor(weather, slope, lie)
        adjusted_distance = round(distance * factor)

        context = {
            'name': name,
            'club': club,
            'distance': distance,
            'weather': weather,
            'slope': slope,
            'lie': lie,
            'adjusted_distance': adjusted_distance,
        }
        return render(request, 'golf/result.html', context)
    
    return render(request, 'golf/form.html')


