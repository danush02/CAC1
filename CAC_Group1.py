import os
import random

#Opening page for users entering application for first time
def homePage():
    print("*"*40)
    print("Welcome to Canteen Order and Payment")
    print("*"*40)
    print("1. Admin\n2. Student")
    role=int(input("Select your Role:"))
    os.system('cls')
    if role==1:
        userHomePage(role)
    elif role==2:
        userHomePage(role)
    else:
        os.system('cls')
        print("Enter a valid number\n")
        homePage()

#Function to display login and login related actions for users
def userHomePage(role):
    if role==1:
        print("Admin Login")
    elif role==2:
        print("Student Login")
    print("-"*20)
    print("Select your action:")
    print("1.Login\n2.Create New User\n3.Forgot Password\n4.Exit")
    action=int(input("Enter the required action:"))
    if action==1:
        userLogin(role)
    elif action==2:
        createNewUser(role)
    elif action==3:
        forgotPassword(role)
    elif action==4:
        exit()
    else:
        os.system('cls')
        print("Enter a valid number\n")
        userHomePage(role)

#Function to display Login page for users
def userLogin(role):
    os.system('cls')
    print("Login Page")
    print("_"*15)
    name=None
    username=input("Username:")
    flag=False
    if role==1:
        for uname in open("adminCredentials.csv","r+").readlines():
            cred=uname.split(",")
            if cred[1]==username:
                flag=True
                name=cred[3]
        if flag==False:
            print("Username is incorrect")
            userLogin()
        else:
            flag=False
            password=input("Password:")
            for cred in open("adminCredentials.csv","r+").readlines():
                passw=cred.split(",")
                if passw[2]==password:
                    flag=True
                    name=passw[3]
            if flag==False:
                print("Password is incorrect")
                userLogin(role)
            else:
                adminLandingPage(name)

    elif role==2:
        for uname in open("studentCredentials.csv","r+").readlines():
            cred=uname.split(",")
            if cred[1]==username:
                flag=True
        if flag==False:
            print("Username is incorrect")
            userLogin(role)
        else:
            flag=False
            password=input("Password:")
            for passw in open("studentCredentials.csv","r+").readlines():
                cred=passw.split(",")
                if cred[2]==password:
                    flag=True
                    name=cred[3]
                    studentId=cred[0]
            if flag==False:
                print("Password is incorrect")
                userLogin(role)
            else:
                studentLandingPage(name,studentId)

def createNewUser(role):
    os.system('cls')
    print("Add New User")
    print("-"*20)
    if role==1:
        name=input("Enter your Name:")
        name=name.strip().title()
        empid=input("Enter you Employee ID:")
        flag=False
        for line in open("adminCredentials.csv","r+").readlines():
            id=line.split(",")
            if id[0]==empid:
                flag=True
        if flag:
            print("User already exist")
            nxt=input("Press enter to continue")
            if nxt=="":
                createNewUser(role)
        else:
            username=name[:4].lower()+str(random.randint(10,99))+str(random.randint(10,99))
            print("Your Username is ",username)
            password=name[:1].lower()+str(random.randint(0,9))+name[1:3]+str(random.randint(100,999))
            print("Your Password is ",password)
            file=open("adminCredentials.csv","a+")
            file.write(empid+","+username+","+password+","+name+"\n")
            file.close()
            userHomePage(role)
    elif role==2:
        flag=False
        name=input("Enter your Name:")
        name=name.strip().title()
        studid=input("Enter you Student ID:")
        for line in open("studentCredentials.csv","r+").readlines():
            id=line.split(",")
            if id[0]==studid:
                flag=True
        if flag:
            print("User already exist")
            nxt=input("Press enter to continue")
            if nxt=="":
                createNewUser(role)
        else:
            department=["MSc Data Science","BA LLB","LLM","BSc Data Science","MBA","BCom"]
            dept=department[int(input("1.MSc Data Science\n2.BA LLB\n3.LLM\n4.BSc Data Science\n5.MBA\n6.BCom\nSelect your Department:"))-1]
            username=name[:4].lower()+str(random.randint(10,99))+str(random.randint(10,99))
            print("Your Username is ",username)
            password=name[:1].lower()+str(random.randint(0,9))+name[1:3]+str(random.randint(100,999))
            print("Your Password is ",password)
            file=open("studentCredentials.csv","a+")
            file.write(studid+","+username+","+password+","+name+","+dept+"\n")
            file.close()
            nxt=input("Press enter to continue")
            if nxt=="":
                userLogin(role)
            
def forgotPassword(role):
    os.system('cls')
    print("Password Recovery Page")
    print("-"*20)
    username=input("Enter your username:")
    if role==1:
        for i in open("adminCredentials.csv","r+").readlines():
            cred=i.split(",")
            if cred[1]==username:
                print("Your password is ",cred[2])
                userLogin(role)
    elif role==2:
        for i in open("studentCredentials.csv","r+").readlines():
            cred=i.split(",")
            if cred[1]==username:
                print("Your password is ",cred[2])
                userLogin(role)

#Function for Landing Page of Admin after login
def adminLandingPage(name):
    os.system('cls')
    print("Admin Page- Welcome! ",name)
    print("_"*20)
    print("Select your action:")
    print("1.Verify Payment\n2.Change Menu\n3.View Orders\n4.Analyse Orders\n5.Logout")
    action=int(input("Your action:"))
    if action==1:
        paymentVerification(name)
    elif action==2:
        changeMenu(name)
    elif action==3:
        viewOrders(name)
    elif action==4:
        analyseOrders()
    elif action==5:
        userHomePage(1)
    else:
        os.system('cls')
        print("Enter a valid number\n")
        adminLandingPage(name)

#Function to verify payment done by student
def paymentVerification(name):
    os.system('cls')
    print("Payment Verification Page")
    print("-"*30)
    flag=False
    paymentId=input("Enter the payment ID:")
    for i in open("orderDetails.csv","r+").readlines():
        details=i.split(",")
        if paymentId in i:
            flag=True
            orderid=details[0]
    if flag:
        print("Payment completed for order ",orderid)
        nxt=input("Press Enter to continue..")
        if nxt=="":
            adminLandingPage(name)
    else:
        print("There is no payment record")
        nxt=input("Press Enter to continue..")
        if nxt=="":
            adminLandingPage(name)
        
def changeMenu(name):
    menu={"mainCourse":[],
    "snacks":[]}
    os.system('cls')
    print("Current Menu")
    print("-"*15)
    slen=0
    for i in open("mainCourseMenu.csv","r+").readlines():
        item=i.split(",")
        if item[0]=="itemName" or item[1]=="itemPrice\n":
            pass
        else:
            menu["mainCourse"].append([item[0],int(item[1])])

    for i in open("snacksMenu.csv","r+").readlines():
        item=i.split(",")
        if item[0]=="itemName" or item[1]=="itemPrice\n":
            pass
        else:
            menu["snacks"].append([item[0],int(item[1])])
    for i in menu["mainCourse"]:
        check=len(i[0])
        if check>=slen:
            slen=check
    print("No."+" "*3+"Dish Name"+" "*(slen-len("Dish Name")+4)+"Price")
    menu["mainCourse"].sort(key=lambda x:x[1],reverse=True)
    sno=0
    for i in menu["mainCourse"]:
        sno+=1
        print(str(sno)+" "*(3-len(str(sno))+3)+i[0]+" "*(slen-len(i[0])+4)+str(i[1]))
    menu["snacks"].sort(key=lambda x:x[1],reverse=True)
    for i in menu["snacks"]:
        sno+=1
        print(str(sno)+" "*(3-len(str(sno))+3)+i[0]+" "*(slen-len(i[0])+4)+str(i[1]))
    print("\n1.Add New Item\n2.Change Item Name\n3.Change Item Price\n4.Back")
    action=int(input("Select your action:"))
    if action==1:
        category=int(input("Enter the Food Category 1.Main Course 2.Snacks:"))
        itemName=input("Enter Item Name:")
        itemPrice=str(input("Enter Item Price:"))
        if category==1:
            file=open("mainCourseMenu.csv","a+")
            file.write(itemName+","+itemPrice+"\n")
            file.close()
            nxt=input("Item added successfully! Press Enter to continue")
            if nxt=="":
                changeMenu(name)
        elif category==2:
            file=open("snacksMenu.csv","a+")
            file.write(itemName+","+itemPrice+"\n")
            file.close()
            nxt=input("Item added successfully! Press Enter to continue")
            if nxt=="":
                changeMenu(name)
    elif action==2:
        category=int(input("Enter the Food Category 1.Main Course 2.Snacks:"))
        itemNum=int(input("Enter the item number:"))
        itemName=input("Enter New Name:")
        if category==1:
            menu["mainCourse"][itemNum-1][0]=itemName
            print(menu["mainCourse"][itemNum-1][0])
            file=open("mainCourseMenu.csv","w+")
            file.write("itemName"+","+"itemPrice"+"\n")
            for i in menu["mainCourse"]:
                file.write(i[0]+","+str(i[1])+"\n")
            file.close()
            nxt=input("Item Name Changed successfully! Press Enter to continue")
            if nxt=="":
                changeMenu(name)
        elif category==2:
            menu["snacks"][itemNum-len(menu["mainCourse"])-1][0]=itemName
            file=open("snacksMenu.csv","w+")
            file.write("itemName"+","+"itemPrice"+"\n")
            for i in menu["snacks"]:
                file.write(i[0]+","+str(i[1])+"\n")
            file.close()
            nxt=input("Item Name Changed successfully! Press Enter to continue")
            if nxt=="":
                changeMenu(name)
    elif action==3:
        category=int(input("Enter the Food Category 1.Main Course 2.Snacks:"))
        itemNum=int(input("Enter the item number:"))
        itemPrice=input("Enter Updated Price:")
        if category==1:
            menu["mainCourse"][itemNum-1][1]=itemPrice
            file=open("mainCourseMenu.csv","w+")
            file.write("itemName"+","+"itemPrice"+"\n")
            for i in menu["mainCourse"]:
                file.write(i[0]+","+str(i[1])+"\n")
            file.close()
            nxt=input("Item Price Changed successfully! Press Enter to continue")
            if nxt=="":
                changeMenu(name)
        elif category==2:
            menu["snacks"][itemNum-len(menu["mainCourse"])-1][1]=itemPrice
            file=open("snacksMenu.csv","w+")
            file.write("itemName"+","+"itemPrice"+"\n")
            for i in menu["snacks"]:
                file.write(i[0]+","+str(i[1])+"\n")
            file.close()
            nxt=input("Item Price Changed successfully! Press Enter to continue")
            if nxt=="":
                changeMenu(name)
    elif action==4:
        adminLandingPage(name)

def studentLandingPage(name):
    os.system('cls')
    print("Student Page- Welcome! ",name)
    print("_"*20)
    print("Select your action:")
    print("1.Create Order\n2.View Transactions\n3.Logout")
    action=int(input("Your action:"))
    if action==1:
        createOrder(0,0,name,[])
    elif action==2:
        viewTransactions()
    elif action==3:
        userHomePage(1)
    else:
        os.system('cls')
        print("Enter a valid number\n")
        studentLandingPage(name)

def createOrder(ch,orderid,name,order):
    os.system('cls')
    if ch==0:
        order=[]
    print("Food Order")
    print("Today's Menu")
    print("-"*30)
    menu={"mainCourse":[],
    "snacks":[]}
    print("Current Menu")
    print("-"*15)
    slen=0
    for i in open("mainCourseMenu.csv","r+").readlines():
        item=i.split(",")
        if item[0]=="itemName" or item[1]=="itemPrice\n":
            pass
        else:
            menu["mainCourse"].append([item[0],int(item[1])])

    for i in open("snacksMenu.csv","r+").readlines():
        item=i.split(",")
        if item[0]=="itemName" or item[1]=="itemPrice\n":
            pass
        else:
            menu["snacks"].append([item[0],int(item[1])])
    for i in menu["mainCourse"]:
        check=len(i[0])
        if check>=slen:
            slen=check
    print("No."+" "*3+"Dish Name"+" "*(slen-len("Dish Name")+4)+"Price")
    menu["mainCourse"].sort(key=lambda x:x[1],reverse=True)
    sno=0
    for i in menu["mainCourse"]:
        sno+=1
        print(str(sno)+" "*(3-len(str(sno))+3)+i[0]+" "*(slen-len(i[0])+4)+str(i[1]))
    menu["snacks"].sort(key=lambda x:x[1],reverse=True)
    for i in menu["snacks"]:
        sno+=1
        print(str(sno)+" "*(3-len(str(sno))+3)+i[0]+" "*(slen-len(i[0])+4)+str(i[1]))
    itemNum=int(input("Enter required item number (Enter 0 to stop order):"))
    if itemNum==0:
        total=0
        print("OrderID:",orderid)
        for line in order:
                print("Item:",line[1],"Quantity:",line[2],"Amount",line[3])
                total=total+int(line[3])
        print("Your total bill amount is ",total)
        payment=input("Pay the bill amount and type 'paid':")
        if payment=="paid":
            paymentid=generatePaymentid()
            print("Your transaction reference number is ",paymentid)
            file=open("orderDetails.csv","a+")
            for line in order:
                print("\nItem:",line[1],"\nQuantity:",line[2],"\nAmount:",line[3])
                total=total+int(line[3])
                file.write(line[0]+","+line[1]+","+str(line[2])+","+str(line[3])+","+str(paymentid)+"\n")
            file.close()
            studentLandingPage(name)
    else:
        itemQuantity=int(input("Enter required quantity:"))
        if (itemNum-1)<=len(menu["mainCourse"]):
            itemPrice=menu["mainCourse"][itemNum-1][1]
            itemName=menu["mainCourse"][itemNum-1][0]
        elif (itemNum-1)>len(menu["mainCourse"]):
            itemPrice=menu["snacks"][itemNum-len(menu["mainCourse"])-1][1]
            itemName=menu["snacks"][itemNum-len(menu["mainCourse"])-1][0]
        if ch==0:
            orderid=generateOrderid()
        order.append([orderid,itemName,itemQuantity,itemPrice*itemQuantity])
        createOrder(ch+1,orderid,name,order)

def generateOrderid():
    rand=[0]*5
    for i in range(0,5):
        rand[i]=str(random.randint(0,9))
    return rand[0]+rand[1]+rand[2]+rand[3]+rand[4]

def generatePaymentid():
    rand=[0]*6
    for i in range(0,6):
        rand[i]=str(random.randint(random.randint(0,5),random.randint(6,9)))
    return rand[0]+rand[1]+rand[2]+rand[3]+rand[4]+rand[5]

def viewOrders(name):
    os.system('cls')
    print("Order Details")
    print("-"*20)
    itemNLen=0
    for i in open("orderDetails.csv","r+").readlines():
        details=i.split(",")
        if len(details[1])>itemNLen:
            itemNLen=len(details[1])
    print("Order ID"+" "*2+"Item Name"+" "*(itemNLen-len("Item Name")+4)+"Quantity"+" "*2+"Amount")
    for i in open("orderDetails.csv","r+").readlines():
        details=i.split(",")
        if details[2]!="quantity":
            print(details[0]+" "*((len("Order ID")-len(details[0]))+2)+details[1]+" "*((itemNLen-len(details[1]))+4)+details[2]+" "*((len("Quantity")-len(details[2]))+2)+details[3])
            nxt=input("Press enter to continue..")
            if nxt=="":
                adminLandingPage(name)
def analyseOrders():
    os.system('cls')
    print("Data Analysis")
    print("-"*20)
    itemNLen=0
    for i in open("orderDetails.csv","r+").readlines():
        details=i.split(",")
        if len(details[1])>itemNLen:
            itemNLen=len(details[1])
    print("Item Name"+" "*(itemNLen-len("Item Name")+4)+"Total Quantity"+" "*2+"Total Amount")
    
homePage()