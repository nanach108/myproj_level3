from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Computers,Phones
from .serializer import ComputersSerializer,PhonesSerializer

# Create your views here.


def index(req):
    return JsonResponse('HELLO ELY FROM VIEWS', safe=False)

def myComputers(req):
    all_products = ComputersSerializer(Computers.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

def myPhones(req):
    all_products = PhonesSerializer(Phones.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

def allMyProducts(req):
    all_computers = ComputersSerializer(Computers.objects.all(), many=True).data
    all_phones = PhonesSerializer(Phones.objects.all(), many=True).data
    return JsonResponse(all_computers+all_phones, safe=False)





# def dollar_sign(req):
#     return ' $'