from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.


# /menu
def index(request):
    """    pizzas = Pizza.objects.all()

    # names
    # pizza_names = [pizza.name for pizza in pizzas]
    # pizza_prices = [[pizza.price for pizza in pizzas]]
    # pizza_names_str = ", ".join(pizza_names)

    # names and prices v1
    # pizza_name_and_prices = []
    # for pizza in pizzas:
    #     pizza_name_and_prices.append(f"{pizza.name} : {pizza.price}")
    # pizza_names_and_prices_str = ", ".join(pizza_name_and_prices)

    # names and prices v2
     pizza_names_and_price = [pizza.name + " : " + str(pizza.price) + "$" for pizza in pizzas]
    pizza_names_and_price_str = ", ".join(pizza_names_and_price)

    return HttpResponse("Our pizza: " + pizza_names_and_price_str)
 """
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas})
