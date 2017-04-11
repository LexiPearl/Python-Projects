import random
class Human(object):                    #-------class
  def __init__(self, clan=None):        #----methods describe what the instance can do, pass self
    print 'New Human!!!'
    self.health = 100
    self.clan = clan
    self.strength = 3
    self.intelligence = 3
    self.stealth = 3
  def taunt(self):
    print "You want a piece of me?"
  def attack(self):
    self.taunt()
    luck = round(random.random() * 100)
    if(luck > 50):
      if((luck * self.stealth) > 150):
        print 'attacking!'
        return True
      else:
        print 'attack failed'
        return False
    else:
      self.health -= self.strength
      print "attack failed"
      return False

# >>> import urllib
# >>> dir(urllib)
# ['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies', '_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', '_noheaders', '_nportprog', '_passwdprog', ...
# >>> help(urllib) # will return a list of information on the given module
#
#
# from my_package.subdirectory import my_functions

# import my_modules.test_module



michael=Human()                         #-----instance

class Cat(object):

garfield = Cat()
garfield.color = "orange"
garfield.type = "fat"
garfield.age = 5
print "Garfield's color:", garfield.color
print "Garfield's type:", garfield.type
print "Garfield's age:", garfield.age

class Cat(object):                      #-----initializing guarantees instance variable exists during the entire life of the project
  def __init__(self, color, type, age):
    self.color = color
    self.type = type
    self.age = age

garfield = Cat('orange', 'fat', 5)
print "Garfield's color:", garfield.color
print "Garfield's type:", garfield.type
print "Garfield's age:", garfield.age
tom=Cat()

class Test(object):
  def __init__(self, phrase='Nothing was passed'):     # set the default value for 'phrase' parameter
    print "This string was passed in: " + phrase
    self.phrase = phrase
test1 = Test('Hello, World!')
test2 = Test()
print "Test 1 has phrase: '" + test1.phrase + "'"
print "Test 2 has phrase, '" + test2.phrase + "'"
