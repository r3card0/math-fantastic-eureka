#

def swap_text(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower() # += concatenar las letras que vayan pasando por cada ciclo
        else:
            result += letter.upper()
    print(result)

if __name__=="__main__":
    swap_text("SEas MAMÓn gueYito")