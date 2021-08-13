def isRightTriangle(a,b,c):
    '''is_right_triangle(a,b,c) -> bool
    returns True if a,b,c is a right triangle with hypotenuse c'''
    
    if a > b and a > c:
        hypotenuse = a
        side1 = b
        side2 = c
    elif b > a and b > c:
        hypotenuse = b
        side1 = a
        side2 = c
    elif c > a and c > b:
        hypotenuse = c
        side1 = a
        side2 = b

    return side1*side1 + side2*side2 == hypotenuse*hypotenuse

print(isRightTriangle(5,3,4))
print(isRightTriangle(3,2,1))
print(isRightTriangle(8,10,6))
print(isRightTriangle(6,8,10))

        

    
