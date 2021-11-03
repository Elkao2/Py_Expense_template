from csv import writer

from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message": "New User - Name",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    user_value = [infos.get('name')]
    with open('users.csv', 'a', newline='') as csvfile:
        writer_object = writer(csvfile)
        writer_object.writerow(user_value)
        csvfile.close()
    return True