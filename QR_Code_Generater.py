from qrcode import QRCode, constants
from colorama import init , Fore, Back
print(Fore.GREEN + '''

  ____        _____          _       _____                           _             
 / __ \      / ____|        | |     / ____|                         | |            
| |  | |_ __| |     ___   __| | ___| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  | | '__| |    / _ \ / _` |/ _ \ | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |__| | |  | |___| (_) | (_| |  __/ |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 \___\_\_|   \_____\___/ \__,_|\___|\_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   

''')

qr = QRCode(
	version=1,
    error_correction=constants.ERROR_CORRECT_H,
	box_size=5,
	border=5
)   


user_input = input(Fore.CYAN + "Enter you string : ")
=======
print('Hello User, this is a program which creates a QR Code for your text. You can use this program to encrypt your text.\n If you want to read the text, simply scan it.')
user_input = input("Enter you string : ")

qr.add_data(user_input)
qr.make(fit=True)


name_for_qrcode = input("Enter Your Name That You Want To Give To The Image Of The QR Code : ")

if 'png' in name_for_qrcode:
    pass
else:
    name_for_qrcode = (name_for_qrcode + '.png')

color_for_qrcode = input("Which Color You Want To Give To Your File(Default:Black): ")

if color_for_qrcode == 'blue' or color_for_qrcode == 'Blue':
    img = qr.make_image(fill_color='blue', back_color='white')
elif color_for_qrcode == 'black' or color_for_qrcode == 'Black':
    img = qr.make_image(fill_color='black', back_color='white')
elif color_for_qrcode == 'red' or color_for_qrcode == 'Red':
    img = qr.make_image(fill_color='red', back_color='white')
elif color_for_qrcode == 'green' or color_for_qrcode == 'Green':
    img = qr.make_image(fill_color='green', back_color='white')
else:
    img = qr.make_image(fill_color='black', back_color='white' )
    print("Invalid Input Choose From: Blue,Black,Red,Green,yellow,white")

img.save(name_for_qrcode)

print('Image Successfully Saved!')
