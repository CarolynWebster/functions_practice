"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


def hello_world():
    """Print Hello World"""
    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


def say_hi(name):
    """Prints greeting with user input name"""
    print "Hi {}".format(name)

# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.


def print_product(num1, num2):
    """Print outcome of num1 multiplied by num1"""
    print num1 * num2

# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times


def repeat_string(repeat_text, num):
    """Creats a single string that takes a string and an integer 
    and prints the string that many times"""
    #create an empty string
    end_string = ""
    #make a var to increment
    num_repeat = num
    #while num_repeat is greater than 0
    while num_repeat > 0:
        #add the string to the end_string
        end_string += repeat_text
        #increment num_repeat down
        num_repeat -= 1
    print end_string

# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".


def print_sign(num1):
    """Prints if input number is higher, lower, or equal to zero"""
    #if higher than zero
    if num1 > 0:
        print "Higher than 0"
    #else if its less than 0
    elif num1 < 0:
        print "Lower than 0"
    #if it's zero, print Zero
    else:
        print "Zero"


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


def is_divisible_by_three(num1):
    """Returns True/False if number if divisible by 3"""
    #get the remainder if the num is divided by 3
    div_remainder = num1 % 3
    #if the remainder of the division is 1 or greater it is not divisible by 3
    if div_remainder >= 1:
        return False
    else:
        return True


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.


def num_spaces(text_string):
    """Returns total number of spaces in the provided string"""
    #split the string based on a space
    split_string = text_string.split(" ")
    #return the length of the list minus 1
    #since there would be one more word than there are spaces
    return len(split_string)-1

# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


def total_meal_price(meal_price, tip=.15):
    #meal total equals the price of the meal times the (tip + 1)
    #equivilant of meal_prince + meal_price * tip
    meal_total = meal_price * (tip + 1)
    return meal_total


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.


def sign_and_parity(num1):
    """Returns list with sign and parity [sign, parity]"""
    num_info = []
    #check for positive or negative
    if num1 >= 0:
        num_info.append("Positive")
    else:
        num_info.append("Negative")
    #check if it's even or odd
    if num1 % 2 == 0:
        num_info.append("Even")
    else:
        num_info.append("Odd")
    #return the list
    return num_info
#unpack the list into two vars
sign, parity = sign_and_parity(5) #Positive, Odd
#print those vars
print "{} {}".format(sign, parity)

###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.


def full_title(name, title="Engineer"):
    """Returns string of name combined with job title"""
    #combine the name and job title - if none given - use Engineer
    return "{} {}".format(title, name)

# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


def write_letter(recipient, job_title, sender):
    """Writes letter to recipient from sender"""
    #use full_title function to get name/title
    name_and_title = full_title(recipient, job_title)
    #print the letter message
    print 'Dear {}, I think you are amazing! Sincerely, {}'.format(name_and_title, sender)

###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
