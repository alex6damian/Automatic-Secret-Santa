import pywhatkit as kit
import pyautogui

def send_msg(phone_numbers, pairs):

    # Mesajul pe care vrei să îl trimiți
    mesaje = []
    for pair in pairs:
        mesaje.append(f"Salutare! La Secret Santa ai prins pe {pair[1]['Nume']}, de la camera {pair[1]['Camera']}, cu urmatorul wishlish: \"{pair[1]['Wishlist']}\" \nCadourile se vor impartii pe data de 5 Decembrie. Seara frumoasa!🎅🎁🎄")
        
    cnt=0

    # Trimite mesajul la fiecare număr din listă
    for phone_number in phone_numbers:
        kit.sendwhatmsg_instantly(phone_number, mesaje[cnt], wait_time=7)  # Trimite mesajul
        pyautogui.press('enter')  # Trimite mesajul apăsând tasta Enter
        cnt+=1