import random
def unluck(member, amount, number_of_member):
    names=list(member.keys())
    for i in names:
        member[i] = amount/(number_of_member)  
    print(member)

def luck(member, amount, number_of_member):
    names=list(member.keys())
    for i in names:
        member[i] = amount/(number_of_member-1)   
    random_key = random.choice(list(member.keys()))
    member[random_key] = 0
    print(random_key + " is the lucky one!")
    print(member)
member={}
number_of_member=int(input("Enter the number of friends joining (including you):"))
if number_of_member>0:
    amount=int(input("Enter the total amount :"))
    while len(member)<number_of_member:
            name=input('Enter name: ')
            member[name]=""
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choise=input()
    if choise=="yes":
        luck(member, amount, number_of_member)
    else:
        unluck(member, amount, number_of_member)
else:
    print("No one is joining for the party")
