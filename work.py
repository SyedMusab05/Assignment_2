#Q1 Area of a triangle: 

base = int(input('Enter base: '))
height = int(input('Enter height: '))

area = (base * height) /2

print(f'the height of a triangle is  {height} and base is {base} and the area of a triangle is  {area}')

#Q2 Calculate average upto2 decimal points

num1 = float(input("Enter Value1: "))
num2 = float(input("Enter Vale2: "))

average = (num1 + num2) / 2

print(f"The average of {num1} and {num2} is: {average:.2f}")

#Q3 Calculate the surface area and volume with the input of a radius

radius = float(input("Enter the radius of the sphere: "))

volume = (4/3) * 3.14159 * radius**3

surface_area = 4 * 3.14159 * radius**2

print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")
print(f"The surface area of the sphere with radius {radius} is: {surface_area:.2f}")
