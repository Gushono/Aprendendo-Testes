from unittest import TestCase, main

def eh_par(val: int) -> bool:
	try:
		return True if val % 2 == 0 else False
	except TypeError:
		return False
		
class Testes(TestCase):
	def test_par(self):
		self.assertEqual(eh_par(2), True)

	def test_impar(self):
		self.assertEqual(eh_par(3), False, "O número não é par")


	def test_string(self):
		self.assertEqual(eh_par('oi '), False)






if __name__ == '__main__':
	main()
