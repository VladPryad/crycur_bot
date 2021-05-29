from datetime import datetime, date, time

def format(res, params):
    pair = params["pair"].upper().split("_")
    date = datetime.now().strftime('%Y.%m.%d %H:%M').replace('.','\.')
    values = ""
    for key in params["action"].split(" "):
        value = str(res[params["pair"]][key]).replace('.','\.')
        values += f"{key}: {value}\r\n"



    result = (f"*{pair[0]} to {pair[1]}*\r\n"
    f"_{date}_\r\n\r\n"
    f"{values}"
    )
    
    return result