from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_stock(request):
    select_stock = {'name': 'Tesla', 'price per share': 11225.50}
    return Response(select_stock)