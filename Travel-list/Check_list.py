swimming = ['swimsuit', 'sunscreen', 'towel', 'snorkling_mask']
dragon_travel = ['passport', 'litter', 'food', 'toy', 'clothes', 'shampoo', 'sponge', 'ear_cleaner', 'eyes_cleaner', 'digestive_pills']
cold_country= ['sweater', 'warm_coat', 'winter_boots', 'winter_pants']
hiking = ['hiking_boots', 'sunscreen']
diving = ['equipment']

# = - an assignment(is)    == - comparison
inp = input('Where are you going:')
if inp == 'swimming':
    print(swimming)
elif inp == 'dragon_travel':
    print(dragon_travel)
else:
    print("Not found")
