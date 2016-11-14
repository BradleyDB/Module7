import pickle #this imports the pickle module
'''This will store the name, grade and location of a climbing route'''
route_name=str(input("Please enter the name of the climbing route: "))
route_grade=input("Please enter the route grade: ")
route_loc=input("Please enter the route location: ")
routelst=[route_name, route_grade, route_loc]

#Now we store the data with pickle.dump
objFile=open("climbingroutes.dat", "ab+")#This opens the file in append/read mode. If the file does not exist it is created
pickle.dump(routelst, objFile)#pickle.dump needs the information to add to the file, and the file as arguments
objFile.close()#closes the connection

#To see the data, you will need to load it back
objFile=open("climbingroutes.dat", "rb")#opens this in read mode
objFiledata=pickle.load(objFile)#the argument .load takes is the file you want data from
objFile.close()

print(objFiledata)
