        if 'what is the time' in query or "what time is this" in query or "can i get the time" in query:
            hour = datetime.datetime.now().hour
            minutes = datetime.datetime.now().minute
            AmPm = "AM"
            if hour > 12:
                hour = hour - 12
                AmPm = "PM"
            strTime = f"{hour} {minutes} {AmPm}"
            speak(f"Sir, It is {strTime}")
        elif "tell me full date" in query or "what date is today" in query or "can you tell me the date" in query:
            allDays = datetime.datetime.now().date()
            day = allDays.strftime("%A")
            hour = datetime.datetime.now().hour
            minutes = datetime.datetime.now().minute
            AmPm = "AM"
            if hour > 12:
                hour = hour - 12
                AmPm = "PM"
            strTime = f"It is {allDays}, {day}, {hour} {minutes} {AmPm}"
            speak(f"Sir, {strTime}")