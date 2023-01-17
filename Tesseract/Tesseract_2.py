from PIL import Image
import pytesseract
import cv2
import sys

imgs = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\Tesseract\dddddd.png') # ocr할 이미지를 imgs 변수에 지정
imge_gray = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY) # imgs에 지정된 이미지를 그레이 스케일로 변환하여 imge_gray로 지정
imge_thr = cv2.threshold(imge_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # 배경에서 전경 텍스트를 분할하기 위해 임계값을 사용한다.

sys.stdout = open('ocr.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
print(pytesseract.image_to_string(imge_thr, lang='kor+eng'))
sys.stdout.close() # 메모장으로 저장

sys.stdout = open('ocr1.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
print(pytesseract.image_to_string(imge_thr, lang='kor'))
sys.stdout.close() # 메모장으로 저장

sys.stdout = open('ocr2.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
print(pytesseract.image_to_string(imge_thr, lang='kor+eng', config='--oem 3 --psm 4 -c preserve_interword_spaces=1'))
sys.stdout.close() # 메모장으로 저장

# path = r'C:\Users\Blackstorm_plecios\Desktop\Tesseract\dddddd.jpg'
# image = cv2.imread(path)

# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# sys.stdout = open('ocr.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
# # print(pytesseract.image_to_string(rgb_image, lang='kor'))
# p = pytesseract.image_to_string(rgb_image, lang='kor')
# p2 = p.rstrip("\n")
# text = (p2)
# print(text)
# sys.stdout.close() # 메모장으로 저장

# file = open(r'C:\Users\Blackstorm_plecios\Desktop\Tesseract\ocr.txt', 'r', encoding="utf-8-sig") # 파일 열기 (처음 사용할 때는 전날 점심.txt 직접 만들어 줘야함)
# p3 = file.read()
# p4 = p3.rstrip("\n") # 불러온 텍스트 뒤에 \n제거

# rgb_image = Image.frombytes('RGB', image.shape[:2], image, 'raw', 'BGR', 0 ,0)
# sys.stdout = open('ocr2.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
# print(pytesseract.image_to_string(rgb_image))
# sys.stdout.close() # 메모장으로 저장

# text = pytesseract.image_to_string(rgb_image, lang='kor')

# sys.stdout = open('ocr.txt', 'w', encoding="utf-8-sig", newline="") # 메모장 오픈
# #print(text)
# sys.stdout.close() # 메모장으로 저장