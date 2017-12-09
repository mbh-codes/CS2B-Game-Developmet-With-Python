#Short Circuits

def returnsTrue():
    print('True')
    return True
def returnsFalse():
    print('False')
    return False
#Example one
returnsFalse() or returnsTrue() #Since the first boolean is False, we need to check the next boolean in the 'or' statement
#Example two
print()
returnsTrue() or returnsFalse() #Since the first boolean is True, we don't have to check the rest of 'or' statement
