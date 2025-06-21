""" Lab 6: OOP and Inheritance"""
import random

# ANSWER QUESTION q1

# ANSWER QUESTION q2

#####################
# Required Problems #
#####################

class PrintModule:
    def pp(self):
        pretty_print(self)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name=name
        self.price = price
        self.stock=0
        self.funds=0
    def vend(self) :
        if self.stock ==0:
            return 'Machine is out of stock.'
        elif self.stock and self.funds<self.price :
            return ('You must add ${0} more funds.'.format(self.price-self.funds))
        elif self.stock and self.funds==self.price :
            self.stock-=1
            self.funds-=self.price
            return 'Here is your {0}.'.format(self.name)
        elif self.stock and self.funds > self.price :
            self.stock-=1
            t=self.funds
            self.funds=0
            return 'Here is your {0} and ${1} change.'.format(self.name,t- self.price)
            
        
    def restock(self, add_stock) :
        self.stock+=add_stock
        return 'Current {0} stock: {1}'.format (self.name, self.stock)
    
    def add_funds(self, ad_funds) :
        
        if self.stock : 
            self.funds+=ad_funds 
            return 'Current balance: ${0}'.format(self.funds)
        else :
            return 'Machine is out of stock. Here is your ${0}.'.format(self.funds+ad_funds)


class Pet:
    """A pet.

    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> kyubey.talk()
    Kyubey
    >>> kyubey.eat('Grief Seed')
    Kyubey ate a Grief Seed!
    """
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)

    def to_str(self):
        "*** YOUR CODE HERE ***"
        return f"({self.name}, {self.owner})"

class Cat(Pet):
    """A cat.

    >>> vanilla = Cat('Vanilla', 'Minazuki Kashou')
    >>> isinstance(vanilla, Pet) # check if vanilla is an instance of Pet.
    True
    >>> vanilla.talk()
    Vanilla says meow!
    >>> vanilla.eat('fish')
    Vanilla ate a fish!
    >>> vanilla.lose_life()
    >>> vanilla.lives
    8
    >>> vanilla.is_alive
    True
    >>> for i in range(8):
    ...     vanilla.lose_life()
    >>> vanilla.lives
    0
    >>> vanilla.is_alive
    False
    >>> vanilla.lose_life()
    Vanilla has no more lives to lose.
    """
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        self.is_alive=True
        self.name=name
        self.owner=owner
        self.lives=lives

    def talk(self):
        """ Print out a cat's greeting.
        """
        "*** YOUR CODE HERE ***"
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        "*** YOUR CODE HERE ***"
        self.lives-=1
        # if self.lives >0:
            
        if self.lives==0:
            self.is_alive=False
        if self.lives<0:
            print(self.name + ' has no more lives to lose.')

    def to_str(self):
        "*** YOUR CODE HERE ***"
        return f"({self.name}, {self.owner},{self.lives})"


class NoisyCat(Cat): # Dose this line need to change?
    """A Cat that repeats things twice.

    >>> chocola = NoisyCat('Chocola', 'Minazuki Kashou')
    >>> isinstance(chocola, Cat) # check if chocola is an instance of Cat.
    True
    >>> chocola.talk()
    Chocola says meow!
    Chocola says meow!
    """
    # def __init__(self, name, owner, lives=9):
    #     # Is this method necessary? If not, feel free to remove it.
    #     "*** YOUR CODE HERE ***"
    #     __init__=Cat.__init__
    
    def talk(self):
        """Talks twice as much as a regular cat.
        """
        "*** YOUR CODE HERE ***"
        print(self.name + " says meow!")
        print(self.name + " says meow!")        



class Colors:
    # 转义序码，ANSI

    HEADER     = '\033[95m'
    OKBLUE     = '\033[34m'
    OKCYAN     = '\033[35m'
    WARNING    = '\033[93m'
    FAIL       = '\033[91m'
    ENDC       = '\033[0m' #颜色重置
    BOLD       = '\033[1m'
    UNDERLINE  = '\033[4m'


def pretty_print(obj):
    """Pretty prints the object using the Colors class.
    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> pretty_print(kyubey)
    \033[34mPet\033[0m\033[35m(Kyubey, Incubator)\033[0m
    """
    "*** YOUR CODE HERE ***"
    output=f"{Colors.OKBLUE}{type(obj).__name__}{Colors.ENDC}{Colors.OKCYAN}{obj.to_str()}{Colors.ENDC}"
    print(output)

class Time:
    """ A class that can store and display the date.
    >>> time = Time(2024, 11, 20)
    >>> print(time.to_str())
    24.11.20
    >>> time.setyear(2023)
    >>> time.setmonth(2)
    >>> time.setday(5)
    >>> time.setformat("dd-mm-yy")
    >>> time.to_str()
    '05-02-23'
    >>> time.setformat("yy/mm/dd")
    >>> time.to_str()
    '23/02/05'
    >>> time.setyear(-1)
    Parameter Error!
    >>> time.to_str()
    '23/02/05'
    """
    def __init__(self, year, month, day):
        """Initialize a Time object."""
        "*** YOUR CODE HERE ***"
        self.year=year
        self.month=month
        self.day=day
        self.format="yy.mm.dd"

    def setyear(self, year):
        """Set the year of the Time object."""
        "*** YOUR CODE HERE ***"
        if not isinstance(year,int) or year < 0:
            print("Parameter Error!")
        else:
            self.year=year

    def setmonth(self, month):
        """Set the month of the Time object."""
        "*** YOUR CODE HERE ***"
        if month<0 or month>12 or not isinstance(month, int):
            return 'Parameter Error!'
        else :
            self.month=month

    def setday(self, day):
        """Set the day of the Time object."""
        "*** YOUR CODE HERE ***"
        if day<0 or day > 31 or not isinstance(day, int):
            return 'Parameter Error!'
        else :
            self.day=day

    def setformat(self, format):
        """Set the format of the Time object."""
        "*** YOUR CODE HERE ***"
        self.format=format

    def to_str(self):
        """Return the formatted date."""
        "*** YOUR CODE HERE ***"
        year=str(self.year)[-2:]
        month=str(self.month).zfill(2)
        day=str(self.day).zfill(2)
        return self.format.replace("yy",year).replace("mm",month).replace("dd",day)