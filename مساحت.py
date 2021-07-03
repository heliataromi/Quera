from math import pi


def get_func(lst):
	dictionary = {'square': square_area, 'circle': circle_area, 'rectangle': rectangle_area, 'triangle': triangle_area}
	result = []
	for shape in lst:
		result.append(dictionary[shape])
	return result


def square_area(edge):
	return edge ** 2


def circle_area(radius):
	return radius ** 2 * pi


def rectangle_area(length, width):
	return length * width


def triangle_area(base, height):
	return base * height * 0.5
