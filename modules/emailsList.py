import os
current_this_file_location = os.path.dirname(__file__)
def chooseEmailAddress(name):
    if 'aacharya' in (name).lower():
        name = str(name).replace('aacharya', 'acharya')
    try:
        email_list_array = []
        file = open(f'{current_this_file_location}\\..\\Data\\emailer.txt', 'r')
        email_list = file.readlines()
        if len(email_list) > 0:
            for email_tup in email_list:
                email_data_list = str(email_tup).replace('\n', '').split("**")
                if str(name).lower() in str(email_data_list[0]).lower():
                    if str(email_data_list[1]).endswith('.com'):
                        get_tuppled = tuple((email_data_list[0], email_data_list[1]))
                        email_list_array.append(get_tuppled)
            return email_list_array
        else:
            return 'no-email-address'
    except FileNotFoundError:
        return 'file-not-found'

def writeEmailAddress(name, email):
    try:
        file = open(f"{current_this_file_location}\\..\\Data\\emailer.txt", 'a')
        file.write("\n{}**{}".format(name, email))
        file.close()
        return True
    except FileNotFoundError:
        return 'file-not-opened'
