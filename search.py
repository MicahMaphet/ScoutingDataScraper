def search(text, find):
    found = 0
    for i in range(len(text)):
        if text[i] == find[found]:
            found += 1
            if found == len(find):
                return True
        else:
            found = 0

    return False

