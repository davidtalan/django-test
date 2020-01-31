from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
import json
from customers.models import Customer
from django.contrib.auth.models import User


class CustomerCollectionView(View):

    def get(self,request):
        data = []
        list_of_customers = list(Customer.objects.all())

        for c in list_of_customers:
            customer = {
            'email': c.user.username,
            'country': c.country
            }
            data.append(customer)

        return JsonResponse({'customers':data})

    def post(self, request):

        try:
            data = json.loads(request.body)
        except Exception as e:
            return HttpResponse(status = 400)

        data_email = data["email"]
        data_password = data["password"]
        data_country = data["country"]

        u = User.objects.create(username = data_email, password = data_password)
        Customer.objects.create(user = u, country = data_country)

        return JsonResponse(data, status = 201)



# TODO: Django app that allows me:
# TODO:- To create a customer
# TODO:- To view all customers
# TODO:To create, I will send a POST request containing email, password and country and it should create a customer
# TODO:To view, I just send a GET request
# TODO:These requests are sent to localhost:8000/customers/
# TODO:Ok, so when you send a GET request to localhost:8000/customers/ you should receive a JSON containing a list of all the customers created so far
# TODO:So in the def get() method you should do a Customer.objects.all()
# TODO:Then format the data, and place it in a JsonResponse
