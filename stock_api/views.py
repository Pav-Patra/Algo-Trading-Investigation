from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from .load_etf import render_graph_html


@api_view(['GET'])
def get_stock(request):
    select_stock = {'name': 'Tesla', 'price per share': 11225.50}
    return Response(select_stock)

# create a function
def simple_view(request):
    context = {"content": "Gfg is the best"}
    return render(request, "test.html", context)

# render raw HTML for incoming asset name
'''
Implemented assets -
etf_list = {
    '0P0000TKZK.L': 'Vanguard_LifeStrategy_60_Equity_Acc',
    '0P0000TKZM.L': 'Vanguard_LifeStrategy_80_Equity_Acc',
    '0P0000KSP6.L': 'Vanguard_FTSE_Dev_Wld_ex-UK_Eq_Idx_Acc',
    '0P000185T3.L': 'Vanguard_Global_Equity_Accumulation',
    'VERE.MI': 'Vanguard_FTSE_Developed_Europe_ex UK_UCITS_ETF_Accuimulation',
    'VMID.SW': 'Vanguard FTSE 250 UCITS ETF',
    'PLTR': 'Palantir Technologies Inc.',
    'NVDA': 'NVIDIA Corporation',
    'MSFT': 'Microsoft Corporation',
    'GOOG': 'Alphabet Inc.'
}
'''

def landing_page_view(request):
    context = {
        "base_url": "http://127.0.0.1:8000/stock_choice/asset/",
        "stock_list": {
            '0P0000TKZK.L': 'Vanguard_LifeStrategy_60_Equity_Acc',
            '0P0000TKZM.L': 'Vanguard_LifeStrategy_80_Equity_Acc',
            '0P0000KSP6.L': 'Vanguard_FTSE_Dev_Wld_ex-UK_Eq_Idx_Acc',
            '0P000185T3.L': 'Vanguard_Global_Equity_Accumulation',
            'VERE.MI': 'Vanguard_FTSE_Developed_Europe_ex UK_UCITS_ETF_Accuimulation',
            'VMID.SW': 'Vanguard FTSE 250 UCITS ETF',
            'PLTR': 'Palantir Technologies Inc.',
            'NVDA': 'NVIDIA Corporation',
            'MSFT': 'Microsoft Corporation',
            'GOOG': 'Alphabet Inc.'
        }
    }
    return render(request, "stock_homepage.html", context)


def asset_graph_view(request, asset_name):
    html = render_graph_html(asset_name)
    return HttpResponse(html, content_type="text/html")