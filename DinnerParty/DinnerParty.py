number_of_member=int(input("Enter the number of friends joining (including you):"))
if number_of_member<=0:
    print("No one is joining for the party")
else:
    amount=int(input("Enter the total amount :"))
    a=round(amount/number_of_member)
    member={}
    while len(member)<number_of_member:
        print('Enter name: ')
        name=input()
        member[name]=a
    print(member)
