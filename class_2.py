# import datetime
# dob = input("Date of Birth: ")
# Year = int(input("Please enter the year you were born: "))
# Month = int(input("Please enter the month you were born: "))
# Day = int(input("Please enter the day you were born: "))

# DOB = datetime.datetime(Year,Month,Day)
# Age = int((datetime.datetime.now()- DOB).days /365)
# print(Age)

# if Age > 21:
#     print("You are old enough to buy this drink")
# elif Age == 21:
#     print("You are old enough to buy this drink")
# else:
#     print("You are not old enough to buy this drink")


#Tenary example
# departments = ("science", "commercial")
# score = 80
# _class = "science" if score> 70 else "commercial"
# print(_class)
 

#HOSPITAL CHECKUP
# csv_file = open("clinic_log.csv", "a")
# name = input("hello what is your name: ")
# print(name, sep = ",", file = csv_file)

# tired_response = input("Are you tired? respond yes/no: ")
# response = True if tired_response == "y" else False 
# print("", "Tired", response, sep = ",", file =csv_file)

# if tired_response == "yes": #check for headache 
#     headache_response = input("Do you have a headache? respond yes/no: ")
#     response = True if headache_response == "y" else False 
#     print("", "Headache", response, sep = ",", file =csv_file)
#     if headache_response == "yes": #check if he has been sleeping well
#         sleep_response = input("Have you been sleeping well? respond yes/no: ")
#         response = True if sleep_response == "y" else False 
#         print("", "Sleeping well", response, sep = ",", file =csv_file)
#         if sleep_response == "yes": #check for fever
#             fever_response = input("Do you have a fever? respond yes/no: ")
#             response = True if fever_response == "y" else False 
#             print("", "Fever", response, sep = ",", file =csv_file)
#             if fever_response == "yes":
#                 print("You have Malaria, please see a doctor")
#             elif fever_response == "no" :#check for no fever
#                 print("Sorry, cant help you")
#         elif sleep_response == "no" :#if not been sleeping well
#             print("you may need to catch some sleep")
#     elif headache_response == "no" :#check for no headache
#         print("Get some food")
# elif tired_response == "no": #check for tiredness
#     print("Why are you now disturbing me?")
# csv_file.close()

# # for x in 'srgetrhyr':
# #     print(x)

# names = ("bade", "bolu", "shayo", "monday")

# for name in names: 
#     print(f"{name.capitalize().ljust(15)}=> {len(name)}")
    




