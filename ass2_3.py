'''
1. code has 5 classes hotel,hotel employee,room,occupant,owner
2. code has init constructor for all 5 classes
3. There are many inheritance's in code for eg. HotelEmployee from hotel, Room from Hotel,  occupant form room, owner from hotel
4. There is a super call in owner class refer to line number:42
5. There is a private data member in code, it is employeepassword in hotel employee class refer to line number:20
6. Multiple Inheritance is used because HotelEmployee and Room are derived from the same base class Hotel Refer lines : 11,15,22
7.all instances or objects are created when user uses all operations in menu tab see lines: 46-74 and the output
'''
class Hotel:
    def __init__(self, name):
        self.hotelname = name

class HotelEmployee(Hotel):
    def __init__(self, name,age,ssn,password,salary):
        self.employeename = name
        self.employeage = age
        self.employeessn = ssn
        self.__employeepassword = password
        self.employeesalary = salary
class Room(Hotel):
    def __init__(self,number,type,status):
        self.roomnumber = number
        self.roomtype = type
        self.roomstatus = status

class Occupant(Room):
    def __init__(self, name,phone,id,roomnumber):
        self.roomnumber=roomnumber
        self.occupantname = name
        self.occupantid = id
        self.occupantphone = phone
    def display(self):
        print(self.occupantname,self.occupantphone,self.occupantid,self.occupantphone,self.roomnumber)

class Owner(Hotel):

    """ I'm the superior of everyone """
    def __init__(self, name,myhotel):
        self.ownername = name
        super().hotelname=myhotel

while True:
    choice= int(input("what do you want to do? \n 1.Add Hotel \n 2.Add Employee \n 3.Add Room \n 4.Add booking \n 5.display booking \n 6.end"))
    if (choice == 1):
        hotelname = input("enter the hotel name")
        a = Hotel(hotelname)
    if (choice == 2):
        employeename = input("enter the employee name")
        employeeage = input("enter the employee age")
        employeessn = input("enter the employee ssn")
        employeepassword = input("enter the employee password")
        employeesalary = input("enter the employee salary")
        b = HotelEmployee(employeename,employeeage,employeessn,employeepassword,employeesalary)

    if (choice == 3):
        roomnumber = input("enter the room number")
        roomtype = input("enter the room type")
        roomstatus = input("enter the room status")
        c = Room(roomnumber,roomtype,roomstatus)

    if (choice == 4):
        customername= input("enter the name of customer")
        customerphone = input("enter the phone number of customer")
        customerid = input("enter the id of customer")
        roomnum = input("enter the room number customer has taken")
        d = Occupant(customername,customerphone,customerid,roomnum)

    if (choice==6):
        break

    if(choice==5):
        d.display()