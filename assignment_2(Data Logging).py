import datetime
c_date = datetime.datetime.now().strftime("%Y%m%d-%H %M %S")
ext = ".txt"

while(True):
    #Taking inputs
    t1 = input('Enter the name:\n')
    if t1 == 'no':
        break
    t2 = int(input("Enter the phone number:\n"))
    t3 = input("Enter the place:\n")
    t4 = int(input("Enter the body temperature:\n"))

    #Storing in a file
    myfile = open(c_date+ext, 'a')
    myfile.write("Name : "+t1.capitalize()+"\n")
    myfile.write("Phone number : "+str(t2)+"\n")
    myfile.write("Place : "+t3.capitalize()+"\n")
    myfile.write("Temperature : "+str(t4)+"'F"+"\n\n")
myfile.close()
