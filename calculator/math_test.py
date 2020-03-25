import pytest
import my_math as math

def setup_module(module):
	#init_something()
	pass

def teardown_module(module):
	#teardown_something()
	pass

def test_add():
	expected = 7
	ret = math.add(2, 5)
	assert ret == expected

def test_add2():
	expected = -3
	ret = math.add(2, -5)
	assert ret == expected

def test_sub():
	expected = -3
	ret = math.sub(2, 5)
	assert ret == expected

def test_sub2():
	expected = 7
	ret = math.sub(2, -5)
	assert ret == expected

def test_mul():
	expected = 10
	ret = math.mul(2, 5)
	assert ret == expected

def test_mul2():
	expected = -10
	ret = math.mul(2, -5)
	assert ret == expected

def test_div():
	expected = 3
	ret = math.div(6, 2)
	assert ret == expected

def test_div2():
	expected = -3
	ret = math.div(6, -2)
	assert ret == expected
