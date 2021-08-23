
def transNum(string):
    number = 1

    numberElements={
        "a":2,"b":2,"c":2,
        "d":3,"e":3,"f":3,
        "g":4,"h":4,"i":4,
        "j":5,"k":5,"l":5,
        "m":6,"n":6,"o":6,
        "p":7,"q":7,"r":7,"s":7,
        "t":8,"u":8,"v":8,
        "w":9,"x":9,"y":9,"z":9,
    }

    for ch in string:
        number = numberElements[ch.lower()]
    return number

def translate(phone):
    newNum = ""
    for ch in phone:
        if ch.lower() in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            newNum = newNum + str(transNum(ch))
        else:
            newNum = newNum + ch
    return newNum

def main():
    phone = input("enter a phone number")
    noLetters = translate(phone)
    print("The number you entered: ", phone)
    print("Translates to: ", noLetters)


