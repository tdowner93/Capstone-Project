from django.shortcuts import render
import random
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ScoreEntryForm
from .models import ScoreEntry

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

@login_required
def scorecard_view(request):
    form = ScoreEntryForm()

    # Handle form submission
    if request.method == 'POST':
        form = ScoreEntryForm(request.POST)
        if form.is_valid():
            score_entry = form.save(commit=False)
            score_entry.user = request.user  # Associate with the logged-in user
            score_entry.save()
            return redirect('scorecard')  # Reload the page to show the new entry

    # Get all the user's scores
    scores = ScoreEntry.objects.filter(user=request.user).order_by('hole_number')

    # Stats calculation
    total_strokes = sum(score.strokes for score in scores)
    total_putts = sum(score.putts for score in scores)
    gir_count = scores.filter(green_in_regulation=True).count()
    fairways_hit_count = scores.filter(fairways_hit=True).count()
    up_and_down_count = scores.filter(up_and_down=True).count()
    holes_played = scores.count()
    average_strokes = round(total_strokes / holes_played, 2) if holes_played > 0 else 0
    average_putts = round(total_putts / holes_played, 2) if holes_played > 0 else 0
    gir_percentage = round((gir_count / holes_played) * 100, 2) if holes_played > 0 else 0
    fairways_percentage = round((fairways_hit_count / holes_played) * 100, 2) if holes_played > 0 else 0
    up_and_down_percentage = round((up_and_down_count / holes_played) * 100, 2) if holes_played > 0 else 0

    context = {
        'form': form,
        'scores': scores,
        'total_strokes': total_strokes,
        'total_putts': total_putts,
        'average_strokes': average_strokes,
        'average_putts': average_putts,
        'gir_percentage': gir_percentage,
        'fairways_percentage': fairways_percentage,
        'up_and_down_percentage': up_and_down_percentage,
        'holes_played': holes_played,
    }

    return render(request, 'scorecard.html', context)

@login_required
def reset_scorecard(request):
    # Delete all scores for the logged-in user
    ScoreEntry.objects.filter(user=request.user).delete()
    
    # After resetting, redirect the user to the scorecard view
    return redirect('scorecard')


@login_required
def home(request):
    return render(request, 'home.html')


