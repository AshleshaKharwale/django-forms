from django.shortcuts import render

from .forms import PizzaForm
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        note = ""
        new_form = PizzaForm()
        if filled_form.is_valid():
            filled_form.save()
            note = "Thanks for ordering! Your pizza is on the way!"
        else:
            note = "Order failed! Please try again."
        return render(request, 'pizza/order.html', {'pizzaform': new_form, 'note': note})
    else:
        pizzaform = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': pizzaform})


