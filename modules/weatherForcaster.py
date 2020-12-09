import wolframalpha # pip install wolframalpha api
app = wolframalpha.Client("PK86X8-P724WU8UQG")

def AskForDetails(query):
    res = app.query(query)
    output = next(res.results).text
    # print(output)
    return output

# AskForDetails("Nepal")