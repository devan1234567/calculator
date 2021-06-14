print ("###############################")
print ("##Welcome to devil calculator##")
print ("###############################")
print ("[1] addition") 
print ("[2] substraction")
print ("[3] multiplication")
def banner():
    print("""╺┳╸╻ ╻┏━┓┏┓╻╻┏    ╻ ╻┏━┓╻ ╻
 ┃ ┣━┫┣━┫┃┗┫┣┻┓   ┗┳┛┃ ┃┃ ┃
 ╹ ╹ ╹╹ ╹╹ ╹╹ ╹    ╹ ┗━┛┗━┛ """)
a = input("Enter an option :")
if a==1 :
        print ("ADDITION")
        ad=int(input("enter first number :"))
        dc=int(input("enter second number :"))
        db=(ad + dc)
        print (db)
        banner()
elif a==2 :
        print ("SUBSTRACTION")
        ad=int(input("enter first number :"))
        dc=int(input("enter second number :"))
        db=(ad - dc)
        print (db)
        banner()
elif a==3 :
        print ("multiplication")
        ad=int(input("enter first number :"))
        dc=int(input("enter second number :"))
        db=(ad * dc)
        print (db)
        banner()
