from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Consume

# Create your views here.
@login_required(login_url='login') 
def dashboardPage(request):
    return render(request, "index.html")

def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
        print(foods)
        
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'index.html', {'foods': foods, 'consumed_food': consumed_food})        

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('dashboard')
    return render(request, 'delete.html')
