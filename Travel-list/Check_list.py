# = - an assignment(is)    == - comparison
import sqlite3

database = sqlite3.connect('Travel_list.db')
cur = database.cursor()

checkList = {
    'swimming' : [
        'swimsuit',
        'sunscreen',
        'towel',
        'snorkling_mask'
    ],
    'dragon_travel' : [
        'passport',
        'litter',
        'food',
        'toy',
        'clothes', 'shampoo', 'sponge', 'ear_cleaner', 'eyes_cleaner',
        'digestive_pills'
    ],
    'cold_country' : [
        'sweater', 'warm_coat', 'winter_boots', 'winter_pants'
    ],
    'hiking' : [
        'hiking_boots', 'sunscreen'
    ],
    'diving' : [
        'equipment'
    ]
}
finalList = []
while True:
    inp = input('Where are you going:')
    inp = inp.strip()

    if inp == 'quit':
        break

    cur.execute('SELECT i.title FROM item i JOIN category c ON i.category_id = c.id WHERE c.title = ? ', (inp,))
    itemResults = cur.fetchall()
    print(itemResults)
    if inp in checkList:
        print('Item added in the final list')
        finalList = finalList + checkList.get(inp)
    else:
        print("Not found")

print(finalList)
