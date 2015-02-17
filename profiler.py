from time import time
from subprocess import call
start = time()
call(["python","hello.py"])
print time() - start
print "Python code ^"
start = time()
call(["java","Hello"])
print time() - start
print "Java code ^"
start = time()
call("./hello")
print time() - start
print "C++ code^"