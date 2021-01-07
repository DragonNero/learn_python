lang = input("Give lang:")
name = input("Give your name:")

def greet(paramLang, paramName):
    if paramLang == "es":
        print("Hola", paramName)
    elif paramLang == "fr":
        print("Bonjour", paramName)
    else:
        print("Hello", paramName)

greet(lang, name)
lang = input("Give lang:")
name = input("Give your name:")
greet(lang, name)
