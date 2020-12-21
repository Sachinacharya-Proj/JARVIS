import random
import datetime
indents = [
    {
        "tags": "greeting",
        "pattern": ['hi','hello', 'how are you', 'hello there', "how's your day",'how are you?',"how is your day","how is your day?", "how's your day?"],
        "response": ['Hello!, I am good, how are you?', "Feeling good!, how's your day?",'I am having fun, I guess. How is your day',"Thanks for stoping by! I really needed someone to talk to"]
    },
    {
        "tags": "time_greeting",
        "pattern": ["good morning","good afternoon","good evening","morning","night","afternoon","evening","good night"],
        "response": ""
    },
    {
        "tags": "personal",
        "pattern": ["do you have a girlfriends?", "do you have a girlfrienD?","do you have girlfriends",'do you have a girlfriend',"do you have a girl friend?","do you have girl friends?", "do you have a girl friend", "do you have girl friends"],
        "response": ["that is none of your buisness", "mind your own buisness", "why would you need that", "are you teasing me?","I am a Machine, I don't have girlfriends", 'lol! go fuck yourself!', 'I am very much single just like my Creator, the great Sachin Acharya, sir!',"knock your arse away, kid", 'why the hell would you ask that', 'I think you have grand enmity with your life, you are askinh this', 'Love, Affection and all this worldly thing just leads ones to desstruction, My Creator and Parents are exception!', "Just go F@@@ yourself","Hell yeah, I don't have one, why don't you find me one, a your are really seems interested finding me one", "Nah, what would I do with Girlfrineds"]
    }
]

# Fallback for Morning time
fallback_morning_pos = ['Good Morning', 'Hi, Good morning!', 'Nice to see you boss, good morning!']
fallback_morning_neg = ["Sorry, It's not morning but anyway good", "ha! you are wrong, it's not morning, good","Good "]

# Fallback for Evening time
fallback_evening_pos = ['Good Evening, sire',"Evening sir,How's your day, sir?","To good to see you sir!, very evening","Always thrilled to see you sir, evening"]
fallback_evening_neg = ["Oh! sir! you need to wake up. It's not evening,but good ","Sorry Sir it isn't evening, anyway good ", "No sir! it's not evening,it is "]

# Fallback for Afternoon time
fallback_afternoon_pos = ['']
fallback_afternoon_neg = ['']

# Fallback for Night time
fallback_night_pos = ['']
fallback_night_neg = ['']

def AppendTimeIdentifier(query):
    dateCondition = datetime.datetime.now().hour
    if dateCondition < 12:
        return f"{query} Morning!"
    elif dateCondition >= 12 and dateCondition <=15:
        return f"{query} Afternoon!"
    elif dateCondition > 15 and dateCondition < 20:
        return f"{query} Evening!"
    else:
        return f"{query} Night!"

def time_greeting(query):
    dateNow = datetime.datetime.now().hour
    if "morning" in query:
        if dateNow < 12:
            return fallback_morning_pos[random.randint(0, len(fallback_morning_pos) - 1)]
        else:
            return AppendTimeIdentifier(fallback_morning_neg[random.randint(0, len(fallback_morning_neg) - 1)])
    elif "afternoon" in query:
        if dateNow >= 12 and dateNow <=15:
            return fallback_afternoon_pos[random.randint(0, len(fallback_afternoon_pos) - 1)]
        else:
            return AppendTimeIdentifier(fallback_afternoon_neg[random.randint(0, len(fallback_afternoon_neg) - 1)])
    elif "evening" in query:
        if dateNow > 15 and dateNow < 20:
            return fallback_evening_pos[random.randint(0, len(fallback_evening_pos) - 1)]
        else:
            return AppendTimeIdentifier(fallback_evening_neg[random.randint(0, len(fallback_evening_neg) - 1)])
    else:
        if dateNow > 18 and dateNow <= 23:
            return fallback_night_pos[random.randint(0, len(fallback_night_pos) - 1)]
        else:
            return AppendTimeIdentifier(fallback_night_neg[random.randint(0, len(fallback_night_neg) - 1)])
    print(dateNow)

def ChatWithMeNow(stringQuery):
    for tag in indents:
        sequence = tag['pattern']
        for seq in sequence:
            stringQuery = stringQuery.lower()
            if seq == stringQuery:    
                if tag['tags'] == "time_greeting":
                    return time_greeting(stringQuery)
                else:
                    indexLevel = random.randint(0, len(tag['response'])-1)
                    return tag['response'][indexLevel]
