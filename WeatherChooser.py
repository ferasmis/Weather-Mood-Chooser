## Author: Feras
## Description: A program to choose what to do today 
##  depending on the weather

weather = input("Enter sunny or cloudy or rainy\n")
if weather == "sunny" :
    print("i will go out")
elif weather == "cloudy":
    print("i will go to a movie")
elif weather == "rainy":
    print("I will stay home")
else:
    print("I will do nothing")
