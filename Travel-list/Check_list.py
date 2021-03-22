# = - an assignment(is)    == - comparison
import sqlite3

database = sqlite3.connect('Travel_list.db')
cur = database.cursor()

finalList = []
while True:
    inp = input('Where are you going:')
    inp = inp.strip()

    if inp == 'quit':
        break

    cur.execute('SELECT i.title FROM item i JOIN category c ON i.category_id = c.id WHERE c.title = ? ', (inp,))
    itemResults = cur.fetchall()
    if len(itemResults) > 0:
        print('Item added in the final list')
        finalList = finalList + list(sum(itemResults, ()))
    else:
        print("Not found")

finalList = list(set(finalList))
print(finalList)
