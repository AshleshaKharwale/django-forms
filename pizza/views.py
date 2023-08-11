from django.shortcuts import render
from django.forms import formset_factory

from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_pizza_form = MultiplePizzaForm()
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        note = ""
        new_form = PizzaForm()
        if filled_form.is_valid():
            pizza_data = filled_form.save()
            pizza_id = pizza_data.id
            note = "Thanks for ordering! Your pizza is on the way!"
        else:
            note = "Order failed! Please try again."
            new_form = filled_form
            pizza_id = None
        return render(request, 'pizza/order.html', {'pizzaform': new_form,
                                                    'note': note,
                                                    'pizza_id':pizza_id,
                                                    'multiple_pizza_form':multiple_pizza_form})
    else:
        pizzaform = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': pizzaform,
                                                    'multiple_pizza_form':multiple_pizza_form})


def edit(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    pizzaform = PizzaForm(instance=pizza)
    if request.method == "POST":
        pizzaform = PizzaForm(request.POST, instance=pizza)
        if pizzaform.is_valid():
            pizzaform.save()
            note = "Order has been updated"
            pizzaform = PizzaForm()
        else:
            note = "Something is wrong! please try again."
        return render(request, 'pizza/edit.html', {'note': note, 'pizzaform': pizzaform})
    return render(request, 'pizza/edit.html', {'pizzaform': pizzaform})


def pizzas(request):
    number_of_pizzas = 2
    filled_form = MultiplePizzaForm(request.GET)
    if filled_form.is_valid():
        number_of_pizzas = filled_form.cleaned_data.get("number_of_pizzas")
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            note = f"{number_of_pizzas} Pizzas have been ordered"
        else:
            note = "Something is wrong. Please try again"
            formset = filled_formset
        return render(request, 'pizza/pizzas.html', {'formset':formset,'note':note})
    return render(request, 'pizza/pizzas.html', {'formset': formset})
