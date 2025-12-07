"""
#When all the length of the sides of the triangle is known - a, b, c
#Semi perimeter (s) = (a+b+c)/2
#Area = square root of (s* (s - a)* (s - b)* (s - c))
"""

#a = float (input("Enter first side of triangle: "))
#b = float (input("Enter second side of triangle: "))
#c = float (input("Enter third side of triangle: "))
#s = (a+b+c)/2
#area  = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#print ("The area of the triangle is ",round(area,2))

"""
When only two sides are known - base , height
Area of the Right angle triangle = 1/2 * base * height
"""
base = float(input("Enter the base side: "))
height = float(input("Enter the height: "))
area = 1/2 * base * height
print ("Area of the right angle triangle = ", area)