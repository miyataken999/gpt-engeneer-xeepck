from django.shortcuts import render, redirect
from .forms import RingForm
from .models import Ring

def ring_info(request):
    if request.method == 'POST':
        form = RingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report')
    else:
        form = RingForm()
    return render(request, 'ring_info.html', {'form': form})

def report(request):
    rings = Ring.objects.all()
    return render(request, 'report.html', {'rings': rings})