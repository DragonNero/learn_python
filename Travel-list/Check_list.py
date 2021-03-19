# = - an assignment(is)    == - comparison
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

while True:
    inp = input('Where are you going:')
    inp = inp.strip()

    if inp == 'quit':
        break

    if inp in checkList:
        print(checkList.get(inp))
    else:
        print("Not found")
