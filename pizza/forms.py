from django import forms
from django.core.exceptions import ValidationError

from .models import Pizza

'''
# Form
class PizzaForm(forms.Form):
    topping1 = forms.CharField(max_length=100)
    topping2 = forms.CharField(max_length=100)
    # size = forms.MultipleChoiceField(label='Size',
    #                                  choices=[('Small', 'Small'),
    #                                         ('Medium', 'Medium'),
    #                                         ('Large', 'Large')],
    #                                  widget=forms.CheckboxSelectMultiple)
    size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'),
                                              ('Medium', 'Medium'),
                                              ('Large', 'Large')],
                             widget=forms.RadioSelect)
    # password = forms.CharField(widget=forms.PasswordInput(), max_length=20)
    # file = forms.FileField()

    def clean_topping1(self):
        data = self.cleaned_data.get('topping1')
        if "olives" in data:
            raise ValidationError("Olives are not accepted")
        return data

    def clean(self):
        topping1 = self.cleaned_data.get('topping1')
        topping2 = self.cleaned_data.get('topping2')
        size = self.cleaned_data.get('size')
        if "cheese" not in topping2:
            raise ValidationError("Cheese is must")
'''


# ModelForm
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Option 1'}
        # widgets = {'size': forms.RadioSelect}
        widgets = {'size': forms.CheckboxSelectMultiple}