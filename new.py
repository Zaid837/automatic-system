# import random
# import sys

# wordList = [
# "lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
#  "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
#            ]

# guess_word = []
# secretWord = random.choice(wordList)
# length_word = len(secretWord)
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# letter_storage = []
# def beginning():
#     print("Hello \n")

#     while True:
#         name = input(" enter Your name\n").strip()

#         if name == '':
#             print(" No blank line")
#         else:
#             break

# beginning()
# def newFunc():
#     print("time to play Hangman!\n")

#     while True:
#         gameChoice = input("Would You?\n").upper()

#         if gameChoice == "YES" or gameChoice == "Y":
#             break
#         elif gameChoice == "NO" or gameChoice == "N":
#             sys.exit( "Have a nice day")
#         else:
#             print("Please Answer only Yes or No")
#             continue

# newFunc()

# def change(): 
#     for character in secretWord: 
#         guess_word.append("-")

#     print("Ok, so the word You need to guess has", length_word, "characters")

#     print("Be aware that You can enter only 1 letter from a-z\n\n")

#     print(guess_word)



# def guessing():
#     guess_taken = 1

#     while guess_taken < 5:
#         guess = input("Pick a letter\n").lower()

#         if not guess in alphabet: 
#             print("Enter a letter from a-z alphabet")
#         elif guess in letter_storage: 
#             print("You have already guessed that letter!")
#         else: 

#             letter_storage.append(guess)
#             if guess in secretWord:
#                 print("You guessed correctly!")
#                 for x in range(0, length_word): 
#                     if secretWord[x] == guess:
#                         guess_word[x] = guess
#                         print(guess_word)

#                 if not '-' in guess_word:
#                     print("You won!")
#                     break
#             else:
#                 print("The letter is not in the word. Try Again!")
#                 guess_taken += 1
#                 if guess_taken == 5:
#                     print(" Sorry Mate, You lost :<! The secret word was",         secretWord)


# change()
# guessing()

# print("Game Over")


# csv_file = open("mean_dev.csv", "w")
# x= 1,2,3,4,5,6,7,9
# y= 10,9,8,7,6,5,4,5
# mean_x = sum(x)/len(x)
# mean_y = sum(y)/len(y)
# x_bar = [i - mean_x for i in x]
# y_bar = [i - mean_y for i in y]

# print(f'{"x".center(8)}|{"y".center(8)}|{"x_bar".center(8)}|{"y_bar".center(8)}|{"Varx".center(8)}')
# print(f'{"x".center(8)},{"y".center(8)},{"x_bar".center(8)},{"y_bar".center(8)}', file =csv_file)
# print(f'{"--------".center(8)}|{"--------".center(8)}|{"--------".center(8)}|{"--------".center(8)}|{"--------".center(8)}')

# for i in range(len(x)):
#     x_val = x[i]
#     y_val = y[i]
#     ybar_val = round(y_bar[i],2)
#     xbar_val = round(x_bar[i],2)
#     Varx = round(Varx[i],2)
    
#     print(f'{str(x_val).center(8)}|{str(y_val).center(8)}|{str(xbar_val).center(8)}|{str(ybar_val).center(8)}')
#     print(f'{str(x_val).center(8)},{str(y_val).center(8)},{str(xbar_val).center(8)},{str(ybar_val).center(8)}', file=csv_file)

# csv_file.close()

# Fruits ={"Banana":"Yellow", "Orange":"orange", "Grapes":"Purple"}
# print("Banana is", Fruits["Banana"])

# target = "Bola"

# guys= {"Bola": {"name":"Bola Idowu","hobby":"playing soccer", "color":Fruits["Banana"]},"Shola":{"name":"Shola badu","hobby":"dancing","color": Fruits["Grapes"]} }
# guys["john"]= {"name": "john joe","hobby":"sleeping","color":Fruits["Orange"]}
# #print("Bola's full name is" ,guys[target]["name"], ",he enjoys", guys[target]["hobby"],"and his best color is", guys[target]["color"])
# print(guys)


import requests
import citylist

api_key = "8ffa2625543f81542dac585e358a40bc"
city_id = "2332453"
cities= citylist.citylist
user_input= input("Enter a city name: ")
def display (city):
    print(city["name"],"--", city["country"])
matched_data= []
for city in cities:
    if user_input in city ["name"]:
        matched_data.append(city)
        display(city)
# print(matched_data)
user_input2= input("Please enter the country code: ")

for city in matched_data:
    if user_input2==city["country"]:
        city_id= city["id"]
        break



url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}"
fetch = requests.get(f"{url}")
data = fetch.json()
weather_data = data["list"]


city_name= data.get("city").get("name")
weather_data = data["list"]
csv_file = open(f"{city_name}.csv", "w")
print("Date","Weather","Temp","Humidity", sep=",", file=csv_file)
for i in weather_data:
    print(i["dt_txt"], i["weather"][0]["description"], i["main"]["temp"], i["main"]["humidity"], sep=",", file=csv_file)
   
csv_file.close()