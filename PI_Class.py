#this program will create a class to collect personal information

#create PersonalInformation superclass
class PersonalInformation:

    #define attributes
    def __init__(self,name,address,age,phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    #define set_name
    def set_name(self, name):
        self.__name = name

    #define set_address
    def set_address(self, address):
        self.__address = address

    #define set_age
    def set_age(self, age):
        self.__age = age

    #define set_phone
    def set_phone(self, phone):
        self.__phone = phone

    #set returns
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone

#create Personal subclass
class Personal(PersonalInformation):

    #define attributes
    def __init__(self,name,address,age,phone):
        PersonalInformation.__init__(self, name, address, age, phone)
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    #define set_name
    def set_name(self, name):
        self.__name = name

    #define set_address
    def set_address(self, address):
        self.__address = address

    #define set_age
    def set_age(self, age):
        self.__age = age

    #define set_phone
    def set_phone(self, phone):
        self.__phone = phone

    #get returns
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone

    #convert strings
    def __str__(self):
        result = 'Name: ' + self.get_name() + '\n' + \
                 'Address: ' + str(self.get_address()) + \
                 '\nAge: ' + str(self.get_age()) + \
                 '\nPhone: ' + str(self.get_phone())
        #return the results
        return result

#create Friends subclass
class Friends(PersonalInformation):

    #define attributes
    def __init__(self,name,address,age,phone):
        PersonalInformation.__init__(name, address, age, phone)
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    #define set_name
    def set_name(self, name):
        self.__name = name

    #define set_address
    def set_address(self, address):
        self.__address = address

    #define set_age
    def set_age(self, age):
        self.__age = age

    #define set_phone
    def set_phone(self, phone):
        self.__phone = phone

    #get returns
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone

    #convert strings
    def __str__(self):
        result = 'Name: ' + self.get_name() + '\n' + \
                 'Address: ' + str(self.get_address()) + \
                 '\nAge: ' + str(self.get_age()) + \
                 '\nPhone: ' + str(self.get_phone())
        #return the results
        return result

#create Family subclass
class Family(PersonalInformation):

    #define attributes
    def __init__(self,name,address,age,phone):
        PersonalInformation.__init__(name, address, age, phone)
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    #define set_name
    def set_name(self, name):
        self.__name = name

    #define set_address
    def set_address(self, address):
        self.__address = address

    #define set_age
    def set_age(self, age):
        self.__age = age

    #define set_phone
    def set_phone(self, phone):
        self.__phone = phone

    #get returns
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone

    #convert strings
    def __str__(self):
        result = 'Name: ' + self.get_name() + '\n' + \
                 'Address: ' + str(self.get_address()) + \
                 '\nAge: ' + str(self.get_age()) + \
                 '\nPhone: ' + str(self.get_phone())
        #return the results
        return result
