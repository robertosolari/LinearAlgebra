from math import sqrt

class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension	 = len(coordinates)
		
		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def plus(self, v):
		new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
		return Vector(new_coordinates)

	def minus(self, v):
		new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
		return Vector(new_coordinates)

	def times_scalar(self, k):
		new_coordinates = [k*x for x in self.coordinates]
		return Vector(new_coordinates)

	def magnitude(self):
		coordinates_squared = [x**2 for x in self.coordinates]
		return sqrt(sum(coordinates_squared))

	def normalization(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(1./magnitude)

		except ZeroDivisionError:
			raise Exception("Cannot normalize the zero vector")


	
	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, v):
		return self.coordinates == v.coordinates

my_vector = Vector([1,2,3])