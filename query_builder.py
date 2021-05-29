from splitter import split
from query import query

def queryBuilder(text):
    params = split(text)
    if(params['pair'] == ""):
        return "No known coins, say again"
    response = query(params)

    return response