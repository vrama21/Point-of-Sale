from django.shortcuts import render, redirect
from .forms import CustomerInfoForm

_customer = {
    'phone_number': '6092043407',
    'first_name': 'Valon',
    'last_name': 'Rama',
    'address_1': '122 S Reeds Rd',
    'address_2': '',
    'city': 'Galloway',
    'zip_code': '08205',
    'comments': 'Apt B around the back'
}


def home(request):
    return render(request, 'pos/home.html')


# def customer_information_blank(request):
#     if request.method == "POST":


def customer_information(request, phone_number=None):
    if request.method == 'POST':
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data.get('phone_number')
            return redirect(phone)
    else:
        form = CustomerInfoForm()
    return render(request, 'pos/customer_information.html', {'form': form})


def new_ticket(request):
    return render(request, 'pos/new_ticket.html')
