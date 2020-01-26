import pytesseract as tess
from PIL import Image
import re
#import time
def con_img_txt(path):
	img = Image.open(str(path))
	print("[+] converting pls wait ..........")
	tess.pytesseract.tesseract_cmd = r'C:/Users/WELCOME/AppData/Local/Tesseract-OCR/tesseract.exe'
	txt_rslt = tess.image_to_string(img)
	print(txt_rslt)
	print("converting to token..........")
	return txt_rslt

def extract(result):
	match_pattern = re.findall(r'([A-z]{4,15}\w+)\s(([A-z]{4,15}\w+))',result)
	print(match_pattern)

result = con_img_txt('lol6.jpg')
print(result)
#time.sleep(8)
extract(result)
with open('test1.txt',mode = 'w') as file:
	print("converting to test1.txt...........")
	file.write(result)

