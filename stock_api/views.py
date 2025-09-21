from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from .asset_load import render_graph_html, get_asset_close_data, get_asset_change


'''
Implemented assets -
'''
all_assets = [
        {'key': '0P0000TKZK.L', 'name': 'Vanguard_LifeStrategy_60_Equity_Acc'},
        {'key': '0P0000TKZM.L', 'name': 'Vanguard_LifeStrategy_80_Equity_Acc'},
        {'key': '0P0000KSP6.L', 'name': 'Vanguard_FTSE_Dev_Wld_ex-UK_Eq_Idx_Acc'},
        {'key': '0P000185T3.L', 'name': 'Vanguard_Global_Equity_Accumulation'},
        {'key': 'VERE.MI', 'name': 'Vanguard_FTSE_Developed_Europe_ex UK_UCITS_ETF_Accuimulation'},
        {'key': 'VMID.SW', 'name': 'Vanguard FTSE 250 UCITS ETF'},
        {'key': 'PLTR', 'name': 'Palantir Technologies Inc.'},
        {'key': 'NVDA', 'name': 'NVIDIA Corporation'},
        {'key': 'MSFT', 'name': 'Microsoft Corporation'},
        {'key': 'GOOG', 'name': 'Alphabet Inc'}
    ]

# render raw HTML for incoming asset name


@api_view(['GET'])
def get_all_assets(request):
    return Response(all_assets)

# django site landing page (use angular frontend one)
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

@api_view(['GET'])
def asset_graph_view(request, asset_name):
    html = render_graph_html(asset_name)
    asset_data = get_asset_close_data(asset_name)
    test_string = f"<h1>Loaded {asset_name}!</h1>"
    jsonAssetResponse = {
        "name": asset_name,
        "graphHtml": test_string,
        "assetDates": asset_data[0],
        "assetClosingPrices": asset_data[1]
    }

    return Response(jsonAssetResponse)

@api_view(['GET'])
def get_percentage_change(request, asset_name, minutes):
    percentage_change = get_asset_change(asset_name, minutes)
    json_response = {
        "assetName": asset_name,
        "percentagePriceChange": percentage_change
    }
    return Response(json_response)

@api_view(['GET'])
def get_all_percent_change(request, minutes):
    response_json = []

    for asset in all_assets:

        try:
            percentChange = get_asset_change(asset['key'], minutes)
        except Exception:
            percentChange = 0.0

        asset_fields = {
            'key': asset['key'],
            'percentChange': percentChange
        }

        response_json.append(asset_fields)

    return Response(response_json)