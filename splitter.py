coins = {}
coins["btc"] = "биток биткоин bitcoin бит"
coins["eth"] = "эфир эфирум"
coins["doge"] = "доге доги dogecoin догекоин додж"
coins["usd"] = "доллар бакс"

params = {}
params["sell"] = "продать продажа сбросить"
params["buy"]  = "купить покупка"



def split(text):
    coin_pair = []
    for key, string in coins.items():
        for value in string.split(" "):
            if(value in text.lower()):
                coin_pair.append(key)

    action = []
    for key, string in params.items():
        for value in string.split(" "):
            if(value in text.lower()):
                action.append(key)

    coin_unique = list(set(coin_pair))
    action_unique = list(set(action))

    result = {}
    result['pair'] = ""
    result['action'] = ""

    if(len(coin_unique) == 0):
        return result

    result['pair'] = f"{coin_unique[0]}_usd"
    if(len(action_unique) == 0):
        result['action'] = "sell buy"
        return result
    
    result['action'] = f"{action_unique[0]}"

    return result