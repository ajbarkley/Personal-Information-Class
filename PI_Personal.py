#this program will create the personal object

#import class
import PI_Class


#main function
def main():

    #make function for list
    personal_info = makePerInfoList()

    #print output
    print('Here is the data entered:')
    display_personal(personal_info)


#function to collect input then store in a list
def makePerInfoList():

    #create empty list
    personal_info = []

    #get inputs for personal information
    Name = input('Enter your name: ')
    Address = input('Enter your address: ')
    Age = input('Enter your age: ')
    Phone = input('Enter your phone: ')
    #blank space
    print()

    #create Personal object to store attributes in
    me = PersonalInformation.Personal(name, address, age, phone)

    #append to list
    personal_info.append(me)

    #return list
    return personal_info

#function to display information
def display_personal(personal_info):
    for info in personal_info:
        print('Personal Information')
        print('Name: ', me.get_name())
        print('Address: ', me.get_address())
        print('Age: ', me.get_age())
        print('Phone: ', me.get_phone())
        #blank space
        print()

#call main
main()
