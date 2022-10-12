def circle_area_circum(radius):
    return radius**2*3.14, 2*3.14*radius

radius=10
area, circum = circle_area_circum(radius)

print('반지름 {}인 원의 면적은 {},원의 둘레는 {:.1f}'.format(radius,area,circum))