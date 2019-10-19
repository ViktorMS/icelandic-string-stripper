def strip(string, replaceWith = " "):

    alphabet = [" ","a","á","b","d","ð","e","é","f","g","h","i","í","j","k","l","m","n","o","ó","p","r","s","t","u","ú","v","x","y","ý","þ","æ","ö"]

    alphabet_string = ""
    
    for character in string:
        if(character.lower() in alphabet):
            alphabet_string += character
        else:
            alphabet_string += replaceWith
    return alphabet_string
        
print(strip("Kennitala 255599-3399..!")) # Kennitala
print(strip("Kennitala 255599-3399..!", replaceWith = "*")) # Kennitala ************** 
