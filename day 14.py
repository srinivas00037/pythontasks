#inheritance
#single inheretance
#one paraent class one child class
class parant:
  p_acres=10000

class child(parant):
    c_acres=500
c1=child()
print(c1.p_acres)
print(c1.p_acres)
 
"supper="#super is used to access the proparties of methods /constuctor in the parant class
class vechicals:
   def __init__(self,milage,wheels):
      self.milage=milage
      self.wheels=wheels
      
class car(vechicals):
   def __init__(self, milage, cc, speed, wheels,):
     super().__init__(milage,wheels)
     self.cc=cc
     self.speed=speed
fararri=car("10km","4","120kmph","100cc")
print(fararri.milage,fararri.speed)
class bike(vechicals):
   def __init__(self, milage, wheels,cc,capacity):
      super().__init__(milage, wheels)
      self.cc=cc
      self.capacity=capacity
ninja=bike("5","4","200cc","1")
print(ninja.milage)



class dog():
   def __init__(self,bread,age):
      self.bread=bread
      self.age=age
   def walking(self):
     return "dog like walking"
class cat():
   def __init__(self,bread,age,color):
       self.bread=bread
       self.age=age
       self.color=color
   def walking(self):
     return "cat can't like walking"
d1=dog("rottweler","1")
print(d1.walking())
c1=cat("bombaay cat","1","black")
print(c1.walking())

#mro:it can be used in first perafance give to b after a and lastlt it will goong to c 

class a:
   name="a"
class b(a):
   name="b"
class c:
    name="c"
class d(b,c):
   pass
d1=d
print(d1.name)


   


    
      
      
      
   
   
