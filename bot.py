import requests
import json

# def __init__(self):
#     h
#     index()
# starting the program
class Start:
    # creating method index to handle all activity in this program
    def index():
        # allow user to insert the URL
        url = input("Enter the URL,  https://")
        # assume user is ok to start execute the program
        ok_value = 'yes'
        # creating a loop which runs 10 times to allow user to enter different values, 10 times.
        for i in range(10):
                # allow user to insert value
                value = input("Enter the value: ")
                myObject = {"url": url, "value": value}
                # most used URL = 1xbet.co.zm
                response= requests.post("https://fast-taiga-60933.herokuapp.com/api/1xbet", data=myObject)

                if(response.text == "404"):
                    Start.check_connection()  
                else:            

                    # print(response.json())
                    json_object = response.json()

                    # json_object = response.json()

                    # for key, value in response.items():
                    #     print(key, "match1", value)

                if ok_value == 'yes':

                    match= "match" 

                    p=int(input("Enter the Investment Cost for match between " + json_object[match]  +" : "))

                    ittr_value1= "match1_over_" + value
                    ittr_value2= "match2_over_" + value

                    ittr_value11= "match1_under_" + value
                    ittr_value22= "match2_under_" + value

                    # a=int(input("Enter the value of chance A1: "))
                    a=json_object[ittr_value1]
                    
                    # b=int(input("Enter the value of chance A2:"))
                    b=json_object[ittr_value11]

                    # d=int(input("Enter the value of chance B1: "))
                    d=json_object[ittr_value2]

                    # e=int(input("Enter the value of chance B2: "))
                    e=json_object[ittr_value22]

                    print(ittr_value1 + ": " +str(a))
                    print(ittr_value11 + ": " +str(b))
                    print(ittr_value2 + ": " +str(d))
                    print(ittr_value22 + ": " +str(e))

                    C1=d*b
                    C2=a*e

                    print("The centre value of Investment A is: ", C1)
                    print("The centre value of Investment B is: ", C2)

                    
                   
                    k1=2*a*C1
                    # escape zero devision
                    if(a == 0):
                        a1=0
                    else:
                        a1=k1/a
                    
                    # escape zero devision
                    if(C1 == 0):
                        C11=0
                    else:
                        C11=k1/C1
                   
                    x=a1 + C11

                    k2=2*d*C2

                    if(d == 0):
                        d1=0
                    else:
                        d1=k2/d
                        

                    # escape zero devision
                    if(C2 == 0):
                        C22=0
                    else:
                        C22=k2/C2
                    
                    y=d1 + C22
                    
                    # escape zero devision 
                    if(x == 0):
                        zz=0
                    else:
                        zz = p/x

                    l=a1*zz
                    m=C11*zz

                    # escape zero devision
                    if(y == 0):
                        ccc=0
                    else:
                        ccc = p/y
                    n=d1*ccc

                    
                    o=C22*ccc

                    w1= l*a
                    R1=w1-p
                    w2= n*d
                    R2=w2-p

                    if w1 > p:
                        print('Cost of Investment A1: ', a ,' is: ',l)
                        print('Cost of Investment C1: ', C1 ,' is: ',m)
                        print('The Profit for Investment A is: ',R1)
                    else:
                        print('Investment A is not valuable and the loss is ',R1)
                    if w2 > p:
                        print('Cost of Investment B1',d ,' is ',n)
                        print('Cost of Investment C2',C2,' is ',o)
                        print('The Profit for Investment B is ',R2)
                    else:
                        print('Investment B is not valuable and the loss is ',R2)

                    ok_value = input("Not satisfied (yes or no): ")


    def check_connection():
        print("Sorry this URL does not exist")
Start.index()
