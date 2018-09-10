# import unittest

def gcd(a,b):
    d = []
    for i in range(1,b+1):
      if(a % i == 0 and b % i == 0):
        d.append(i)
    max_index = len(d)-1
    return d[max_index]

# class Mytest(unittest.TestCase):
#   def test(self):
#     self.assertEqual(gcd(50,51),1)

# if __name__ = __main__:
#     unittest.main()

if __name__ == '__main__':
    assert 1 == gcd(50,51)
    assert 3 == gcd(6,9)
    assert 10 == gcd(10,50)
    assert gcd(25,30) == 5

print("Test Success")
