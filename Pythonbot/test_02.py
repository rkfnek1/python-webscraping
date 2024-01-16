# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#     print(f"your bmi is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"your bmi is {bmi}, you have a normal")
# elif bmi < 30:
#     print(f"your bmi is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"your bmi is {bmi}, you are obese.")
# else:
#     print(f"your bmi is {bmi}, you are clinically obese.")

# --------------------------------------------------------------------------------------------------

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# --------------------------------------------------------------------------------------------------

# import random

# a = ["", "", "", "", ""]

# b = random.choice(a)

# print(b)

import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

first_article = soup.find('ul', {'class': 'section_list_ranking'}).find('li').find('a')['href']

print(first_article)