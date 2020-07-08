from django.shortcuts import render
from .models import Meals
# Create your views here.
def meal_list(request):
    meal_list=Meals.objects.all()
    context={'meal_lsit':meal_list,}
    return render(request,'meal/list.html',context)

def meal_detail(request,slug):
    pass
