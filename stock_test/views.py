from django.shortcuts import render
from django.http import HttpResponse

def stock_test(request):
    return HttpResponse("Hello yFinance!!")