from django.shortcuts import render

# Create your views here.

def all_proj(request):
    return render(request, 'proj_2/all_index.html')
