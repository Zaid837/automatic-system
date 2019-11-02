# def useless(name,age,class_):
#     print(f"Hi {name}, welcome to the {class_} class, you are {age} years old")
# useless("John",19,"first")
# useless("first","John",19)
# useless(name="John",age="19",class_="first")
# useless(age="19",name="John",class_="first")

# def func(a,b,c):
#     print(f"A={a},B={b},C={c}")
# func()

# def func(a=10,b=20,c=30):
#     print(f"A={a},B={b},C={c}")
# func()

# def func(a=10,b=20,c=30):
#     print(f"A={a},B={b},C={c}")
# func(a=50)


# def mean (_list):
#     mean= sum(_list)/len(_list)

#     return mean

# def variance(_list, mean):
#         variance_value = [n-mean(_list) for n in _list]
#         squared_variance = [n **2 for n in variance_value]

#         return variance_value,squared_variance

# numbers=[1,2,5,10,20]
# mean_of_numbers= mean(numbers)
# print(mean_of_numbers)

# variance_of_nums = variance(numbers,mean)
# print(variance_of_nums)


# names = [
#     {
#         "name": "ade",
#         "age": 20,
#         "score": 60
#     },
#     {"kunle":
#     {
#     "name": "kunle",
#     "age": 50,
#     "score": 20
#     }},
#     {"shade":
#     {
#     "name": "shade",
#     "age": 70,
#     "score": 30
#     }}
#     ]

# def get_ages(_list):
#     ages = [i['age'] for i in _list]
#     scores= [i['score'] for i in _list]
#     return {'ages': ages, 'scores': scores}

# ages = get_ages(names)
# print(ages['scores'])


#positional argunments
# mylist=[10,5,15,5]
# def function(ag1,ag2):
#     mult= ag1 * ag2
#     print(mult)

# function(mylist,4)

# # #variable positional argunments

# def function2(*args):
#     print(args)
#     print(type(args))

# function2(*mylist)

#variable keyword argunments
# def function3(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# function3(x=10,y=20,z=30)...
# numbers = range(10,100,5)
# def test(*numbers,divisor):
#     num.list=[]
#     for number in numbers:
#         if number % divisor ==0:
#             num.list.append[]
#             print(number)

# test(*numbers, divisor=2)



# def get_t_amount(**goods):
#     print(goods)
#     total = 0
    
#     for key in goods.copy():
#         #print(goods[key])
#         total_amount= goods[key] *20
#         total += total_amount

#         goods[key]= total_amount
#     goods['total']= total
#     print(goods)
    
# get_t_amount(box=2,shoe =3, socks =4)



import requests
url= "http://checklight.pythonanywhere.com/get_readings/1x0d001/1/"
response = requests.get(url)
#print(response)
data= response.json()
print(data["streets"][0])

# class Dog():
#     legs=4
#     tails= 1
#     color= "brown"

#     def bark(self):
#         sound="woof"
#         print(sound)

# new_dog= Dog()
# print(new_dog.legs)
# print(new_dog.tails)
# print(new_dog.color)
# new_dog.bark()



# class Acct():
#     __bal = 0

#     def __init__(self, name, bvn):
#         self.name =name
#         self.bvn =bvn

# new_acct = Acct("john".345697878)
# new_acct.__bal = 2000000


# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):

#         self.name = name
#         self.age = age


# missy = Cat('Missy', 3)
# lucky = Cat('Lucky', 5)

# print(missy.name, missy.age)
# print(lucky.name, lucky.age)

# print(Cat.species)
# print(missy.__class__.species)
# print(lucky.__class__.species)

# class Car:
#     def brake(self):
#         print("Brakes")

#     def accelerate(self):
#         print("Accelerating")

# car1 = Car()
# car1.color = "Red"
# car1.brake()


# class new_car(Car):
#     def __init__(self,brand, model, year):
#         # Sets all the properties
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start_car(self):
#         """ Start the cars engine """
#         print ("vroem vroem")

# if __name__ == "__main__":
#     # Creates two instances of new_car, each with unique properties
#     car1 = new_car("Ford","F-150",2001)
#     car2 = new_car("Toyota","Corolla",2007)

#     car1.start_car()
#     car2.start_car()