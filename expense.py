import csv
from csv import writer

from PyInquirer import prompt

def get_user_list():
    users = []
    with open('users.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            users.append(row)
        print(users)
        csvfile.close()
    user_list = []
    for elt in users:
        user_list.append(elt[0])
    return user_list

def get_user_checkbox(spender):
    user_list = get_user_list()
    user_checkbox = []
    for elt in user_list:
        dictionary = {}
        dictionary["name"] = elt
        if (elt == spender):
            dictionary["checked"] = True
        user_checkbox.append(dictionary)
    print(user_checkbox)
    return user_checkbox



def get_involved_user(spender):
    get_involved = [
        {
        "type":"checkbox",
        "name":"involved",
        "message": "Users involved for this expense",
        "choices": get_user_checkbox(spender),
    },
    ]
    infos = prompt(get_involved)
    print(infos)
    return infos.get("involved")


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_user_list()
    },
]
def new_expense(*args):

    with open('expense_report.csv', 'a', newline= '') as csvfile:
        infos = prompt(expense_questions)
        involved_user = get_involved_user(infos.get('spender'))
        expense_value = [infos.get('amount'), infos.get('label'), infos.get('spender'), involved_user]
        writer_object = writer(csvfile)
        writer_object.writerow(expense_value)
        csvfile.close()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


