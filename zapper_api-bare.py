import requests

#--- function to get token balances from zapper fi ---#
def token_balances(wallet_address):
    api_url = 'https://api.zapper.fi/v1/protocols/tokens/balances?addresses%5B%5D='+wallet_address+'&network=ethereum&api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241'
    r = requests.get(api_url)
    api_data = r.json()
    tokens = api_data[wallet_address]['products'][0]['assets']

    data = dict()

    for this_token in tokens:
        this_currency = this_token['symbol']
        this_balance = this_token['balance']
        data[this_currency] = this_balance

    return data
#--- end function to get token balances from zapper fi ---#

wallet = '0x0000000000000000000000000000000000000000'

balances = token_balances(wallet)
print(balances)
