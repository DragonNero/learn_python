# pet dictionary to hold our pet's parameters# pet dictionary to hold our pet's parameters
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "playfulness": 0, "toys": []}

# Handle quitting the game, printing out resulting information
def quitSimulator():
  print("That's the end of the game! Thank you for playing the pet simulator!")

# Feed your pet utilizing current supplies
def feedPet():
  # Set the pet's hunger level to the decreased hunger
  newHunger = pet["hunger"] - 10
  if newHunger < 0:
    newHunger = 0
  pet["hunger"] = newHunger
  print("Fed your pet! Hunger decreased by 10.")

# Create a dictionary of pets and their associated toys that they can use
petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"], "dog": ["chew toy", "stick", "frisbee"], "fish": ["undersea castle", "fake coral", "buried treasure"] }

# Get your pet a new toy
def getToy():
  toyChoices = petToys[pet["type"]]
  toyNum = -1
  while toyNum < 0 or toyNum >= len(petToys):
    print("Here are your toy choices: ")
    for i in range(len(toyChoices)):
      print(str(i) + ": " + toyChoices[i])

    toyNum = int(input("Please input your choice of pet toy: "))

  # Get the chosen toy as a string
  chosenToy = toyChoices[toyNum]

  # add it to the list of toys
  pet["toys"].append(chosenToy)
  print("Nice! You chose: " + chosenToy + " for " + pet["name"] + ". Great pick!")

# Play with the toys
def playToys():
  print("Yay! Let's play with our toys.")
  pet["playfulness"] += 10

# Function to print the menu
def printMenu(menuOptions):
  print()
  print("Here is the current menu of options you have:")
  print("----------")

  # iterate through the menu options, printing out the key meant to be pressed, along with its corresponding text
  for key in menuOptions:
    print(key + ":\t" + menuOptions[key]["text"])

  # print an additional newline character
  print()

# Prints stats about the pet
def printStats():
  print()
  print("Your " + pet["type"] + " named " + pet["name"] + " had a great time playing with you!")
  print(pet["name"] + " is " + str(pet["age"]) + " days old")
  print(pet["name"] + " is currently at a hunger level of " + str(pet["hunger"]) + " out of 100!")
  print("You have " + str(len(pet["toys"])) + " toys! They are: ")
  for toy in pet["toys"]:
    print(toy)
  print()

# Handle initializing our pet, with its food, thirst, fun level
def initPet(petToys):

  # Extract the possible pets into a list for easier references
  petOptions = list(petToys.keys())

  # Initialize selectedPet in order to continue prompting for pets if choice given wasn't in the dictionary
  selectedPet = ""

  # Loop through pets
  while selectedPet not in petOptions:
    print("Your options of pets are: ")
    for option in petOptions:
      print(option)

    selectedPet = input("Please select one of these pets. Which one would you like? ")

    if selectedPet not in petOptions:
      print("Sorry! That wasn't one of our options.")

  # Store pet type in dictionary
  pet["type"] = selectedPet

  # Prompt and store pet name
  petName = input("Great! You've selected a pet, now please name your pet! ")
  pet["name"] = petName

# Main loop that controls our program logic
def main():
  # Initialize our pet
  initPet(petToys)

  # Options in the menu and their corresponding function to invoke
  menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game"}, "F": { "function": feedPet, "text": "Feed " + pet["name"] + "!"}, "G": { "function": getToy, "text": "Get a toy for " + pet["name"] + "!"}, "P": { "function": playToys, "text": "Play with " + pet["name"] + " and your toys!"} }

  # Enter main loop of the simulator
  keepPlaying = True
  while keepPlaying:
    menuSelection = ""
    menuOptionsKeys = list(menuOptions.keys())

    while menuSelection not in menuOptionsKeys:
      # Print out the possible options
      printMenu(menuOptions)

      # Get the response, lowercase
      menuSelection = input("Which option will you select? ").upper()
      print()

    # Handle quitting from the simulator
    if menuSelection == "Q":
      keepPlaying = False

    # Invoke the function associated with the menu selection
    menuOptions[menuSelection]["function"]()

    # Increment pet variables
    pet["hunger"] += 3
    pet["age"] += 1

    # Print stats after
    printStats()

main()
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "playfulness": 0, "toys": []}

# Handle quitting the game, printing out resulting information
def quitSimulator():
  print("That's the end of the game! Thank you for playing the pet simulator!")

# Feed your pet utilizing current supplies
def feedPet():
  # Set the pet's hunger level to the decreased hunger
  newHunger = pet["hunger"] - 10
  if newHunger < 0:
    newHunger = 0
  pet["hunger"] = newHunger
  print("Fed your pet! Hunger decreased by 10.")

# Create a dictionary of pets and their associated toys that they can use
petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"], "dog": ["chew toy", "stick", "frisbee"], "fish": ["undersea castle", "fake coral", "buried treasure"] }

# Get your pet a new toy
def getToy():
  toyChoices = petToys[pet["type"]]
  toyNum = -1
  while toyNum < 0 or toyNum >= len(petToys):
    print("Here are your toy choices: ")
    for i in range(len(toyChoices)):
      print(str(i) + ": " + toyChoices[i])

    toyNum = int(input("Please input your choice of pet toy: "))

  # Get the chosen toy as a string
  chosenToy = toyChoices[toyNum]

  # add it to the list of toys
  pet["toys"].append(chosenToy)
  print("Nice! You chose: " + chosenToy + " for " + pet["name"] + ". Great pick!")

# Play with the toys
def playToys():
  print("Yay! Let's play with our toys.")
  pet["playfulness"] += 10

# Function to print the menu
def printMenu(menuOptions):
  print()
  print("Here is the current menu of options you have:")
  print("----------")

  # iterate through the menu options, printing out the key meant to be pressed, along with its corresponding text
  for key in menuOptions:
    print(key + ":\t" + menuOptions[key]["text"])

  # print an additional newline character
  print()

# Prints stats about the pet
def printStats():
  print()
  print("Your " + pet["type"] + " named " + pet["name"] + " had a great time playing with you!")
  print(pet["name"] + " is " + str(pet["age"]) + " days old")
  print(pet["name"] + " is currently at a hunger level of " + str(pet["hunger"]) + " out of 100!")
  print("You have " + str(len(pet["toys"])) + " toys! They are: ")
  for toy in pet["toys"]:
    print(toy)
  print()

# Handle initializing our pet, with its food, thirst, fun level
def initPet(petToys):

  # Extract the possible pets into a list for easier references
  petOptions = list(petToys.keys())

  # Initialize selectedPet in order to continue prompting for pets if choice given wasn't in the dictionary
  selectedPet = ""

  # Loop through pets
  while selectedPet not in petOptions:
    print("Your options of pets are: ")
    for option in petOptions:
      print(option)

    selectedPet = input("Please select one of these pets. Which one would you like? ")

    if selectedPet not in petOptions:
      print("Sorry! That wasn't one of our options.")

  # Store pet type in dictionary
  pet["type"] = selectedPet

  # Prompt and store pet name
  petName = input("Great! You've selected a pet, now please name your pet! ")
  pet["name"] = petName

# Main loop that controls our program logic
def main():
  # Initialize our pet
  initPet(petToys)

  # Options in the menu and their corresponding function to invoke
  menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game"}, "F": { "function": feedPet, "text": "Feed " + pet["name"] + "!"}, "G": { "function": getToy, "text": "Get a toy for " + pet["name"] + "!"}, "P": { "function": playToys, "text": "Play with " + pet["name"] + " and your toys!"} }

  # Enter main loop of the simulator
  keepPlaying = True
  while keepPlaying:
    menuSelection = ""
    menuOptionsKeys = list(menuOptions.keys())

    while menuSelection not in menuOptionsKeys:
      # Print out the possible options
      printMenu(menuOptions)

      # Get the response, lowercase
      menuSelection = input("Which option will you select? ").upper()
      print()

    # Handle quitting from the simulator
    if menuSelection == "Q":
      keepPlaying = False

    # Invoke the function associated with the menu selection
    menuOptions[menuSelection]["function"]()

    # Increment pet variables
    pet["hunger"] += 3
    pet["age"] += 1

    # Print stats after
    printStats()

main()
