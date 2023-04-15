
# Searches a string for a string
def search(text, find):
    found = 0 # keep track of the portion of the string found
    for i in range(len(text)): # loop over the string
        if text[i] == find[found]: # check for expected character
            found += 1
            if found == len(find): # if the entire string has been found
                return True # the string has been found
        else:
            found = 0 
    return False
