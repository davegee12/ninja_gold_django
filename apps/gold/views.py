from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "gold/index.html")

# def process_money(request):
#     request.session['count'] += 1
#     if request.method == "POST":
#         if request.POST['name'] == 'farm':
#             farm_gold = int(random.randint(10,20))
#             print(farm_gold)
#             request.session['gold'] += farm_gold
#     return redirect("/")

def farm(request):
    request.session['count'] += 1
    farm_gold = int(random.randint(10,20))
    print(farm_gold)
    request.session['gold'] += farm_gold
    request.session['activities'].insert(0, "<div class='green'> Earned " + str(farm_gold) + " gold pieces from your farm!</div>")
    return redirect("/")

def cave(request):
    request.session['count'] += 1
    cave_gold = int(random.randint(5,10))
    print(cave_gold)
    request.session['gold'] += cave_gold
    request.session['activities'].insert(0, "<div class='green'> Earned " + str(cave_gold) + " gold pieces from the cave!</div>")
    return redirect("/")

def house(request):
    request.session['count'] += 1
    house_gold = int(random.randint(10,20))
    print(house_gold)
    request.session['gold'] += house_gold
    request.session['activities'].insert(0, "<div class='green'> Earned " + str(house_gold) + " gold pieces from your house!</div>")
    return redirect("/")

def casino(request):
    request.session['count'] += 1
    casino_gold = int(random.randint(0,50))
    print(casino_gold)
    give_take = random.randint(0,1)
    print("give_take = " + str(give_take))
    if give_take == 0:
        request.session['gold'] += casino_gold
        request.session['activities'].insert(0, "<div class='green'> Won " + str(casino_gold) + " gold pieces at the casino!</div>")
    if give_take == 1:
        request.session['gold'] -= casino_gold
        request.session['activities'].insert(0, "<div class='red'> Lost " + str(casino_gold) + " gold pieces at the casino!</div>")
    return redirect("/")

def reset(request):
    if request.method == "POST":
        del request.session['count']
        del request.session['gold']
        del request.session['activities']
    return redirect("/")
