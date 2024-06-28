#  Question : Write a program that takes user age as input and prints whether the person is a child, teenager, adult or senior.


user_age = input("Enter your age: \n")
user_age_in_int = int(user_age)

if(user_age_in_int <13):
    print("++User is Child++")
elif(user_age_in_int >13 and user_age_in_int<19):
    print("++User is Teenager++")
elif(user_age_in_int > 20 and user_age_in_int <59):
    print("++User is Adult++")
else:
    print("++User is Senior++")