mail_list = [
    {
        "name": "Sachin Acharya",
        "add": "acharyaraj9865032909@gmail.com"
    },
    {
        "name": "Sachin Acharya",
        "add": "acharyaraj71@gmail.com"
    },
    {
        "name": "Sachin Acharya",
        "add": "rohitgupta36000@gmail.com"
    },
    {
        "name": "Dipak Tamang",
        "add": "dipak123tmg@gmail.com"
    },
    {
        "name": "Aalok Pariyar",
        "add": "alokpariyar71@gmail.com"
    },
    {
        "name": "ram lal",
        "add": "clear your name"
    }
]

intialArray = []
def findemails(name):
    if "aacharya" in name:
        name = name.replace("aacharya", "acharya")
    for child in mail_list:
        if name in child["name"].lower():
            getTuppled = (child["name"], child["add"])
            intialArray.append(getTuppled)
    return intialArray