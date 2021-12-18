number_of_member=int(input("Enter the number of friends joining (including you):"))
def getDict():
    member={}
    while len(member)<number_of_member:
        print('Enter name: ')
        name=input()
        member[name]=0
    print(member)
 
getDict()

