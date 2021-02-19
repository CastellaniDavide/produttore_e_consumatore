"""Test produttore_e_consumatore file
"""
from produttore_e_consumatore import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-2-19"

def test():
	"""Tests the produttore_e_consumatore function in the produttore_e_consumatore class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert produttore_e_consumatore.produttore_e_consumatore() == "produttore_e_consumatore", "test failed"
	#assert produttore_e_consumatore.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
