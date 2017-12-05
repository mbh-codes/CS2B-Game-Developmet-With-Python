# None Value and Short Circuits

#value = print("") #
#print(value)

def returnsTrue():
    print('True')
    return True
def returnsFalse():
    print('False')
    return False

#returnsFalse() or returnsTrue()
returnsTrue() or returnsFalse()
