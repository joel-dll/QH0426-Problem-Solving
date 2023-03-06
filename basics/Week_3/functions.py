# Parameter - data given/inject into the function
#def t_area(basse, height):
   # h=float(input("\nEnter the height: "))
   # b= float(input("Enter the base: "))
   # area = h*b*0.5
   # print("The area of this triangle is {}".format(area))

#t_area() #call the function or creat a for loop
#t_area()#

# default parameters - assumed if nothing is provided as argument
# Return values - data extracted from a function into the space where function was

x=7 #scoope
def t_area(base = 1,height = 2):
    area = height*base*0.5
    area +=7
    return area

x = t_area()
y = t_area(10,7) #call the function with arguments
z = t_area(18)
a = t_area(height = 8)


print("The area of this triangle is {}".format(x+y+z+a))
print(t_area(10,10))