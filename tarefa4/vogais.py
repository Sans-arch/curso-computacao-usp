def vogal(carac):
    if (carac == "A" or carac == "a"):
        return True
    if (carac == "E" or carac == "e" ):
        return True
    if (carac == "I" or carac == "i"):
        return True
    if (carac == "O" or carac == "o"):
        return True
    if (carac == "U" or carac == "u"):
        return True
    return False

print(vogal("b"))