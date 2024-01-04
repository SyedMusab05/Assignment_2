area = (base * height) / 2
return area
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle_area = calculate_triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is: {triangle_area}")
