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

def test_vogal_a():
    assert vogal("a") == True
    
def test_vogal_b():
    assert vogal("b") == False
    
def test_vogal_e():
    assert vogal("E") == True
    
def test_vogal_u():
    assert vogal("u") == True

def test_vogal_x():
    assert vogal("X") == False
