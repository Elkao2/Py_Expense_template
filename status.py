import csv
from csv import writer
from expense import get_user_list



def get_status():
    user_list = get_user_list()
    user_spend = []
    for user in user_list:
        user_spend.append((user, 0))
    print(user_spend)
    file_line = []
    with open('expense_report.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            file_line.append(row)
        csvfile.close()
    for elt in file_line:
        amount = elt[0]
        user_spend.append([elt[2], int(amount)])
        amount_by_user = int(amount) // len(elt[3])
        print(elt)
        print(elt[3][0])
        for user in elt[3]:
            user_spend.append([user, - amount_by_user])
    return True