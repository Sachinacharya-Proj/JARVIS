import wolframalpha # pip install wolframalpha api
import os

client_api = os.environ.get('WHEATHER_API')

app = wolframalpha.Client(client_api)

def AskForDetails(query):
    res = app.query(query)
    output = next(res.results).text
    return output

