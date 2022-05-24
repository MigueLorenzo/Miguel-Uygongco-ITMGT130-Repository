'''Assignment 1

This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.

This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1.
    Factorial. 1 point.

    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.

    Parameters
    ----------
    x: int
        the integer whose factorial to return

    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line
if x==1:
    return 1
else:
    return (x * factorial(x-1))
print("The factorial of the argument is "+ str(factorial(5)))

def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.

    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9

    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.

    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line
if number_grade >=92 and number_grade <= 100:
    return("A")
elif number_grade >=86 and number_grade <=91.9:
    return("B+")
elif number_grade >=80 and number_grade <=85.9:
    return("B")
elif number_grade >=74 and number_grade <=79.9:
    return("C+")
elif number_grade >=67 and number_grade <=73.9:
    return("C")
elif number_grade >=60 and number_grade <=66.9:
    return("D")
elif number_grade >=0 and number_grade <=59.9:
    return("F")
number_grade = float(input("Enter Grade: "))
print("The letter grade equivalent of the number grade is " + classify_grade(number_grade))

def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.

    You have purchased two bags of items.
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.

    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.

    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line
return (item_weight_1* item_quantity_1 + item_weight_2 * item_quantity_2)/(item_quantity_1+item_quantity_2)
print ("The weighted average weight of one item is ")
print (average_weight(1, 2, 3, 4))

def string_sum(string):
    '''Item 4.
    String Sum. 3 points.

    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.

    Parameters
    ----------
    string: str
        a string that can contain any character.

    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line
def sum_digits(str):
    sum = 0
    for x in str:
        if x.isdigit() == True:
            sum += int(x)
    return sum

your_str = input("Enter an alphanumeric string : ")
print(sum_digits(your_str))


def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.

    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum

    You may want to import the `math` library for this number.

    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate

    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line
import math
x_1 = float(input("Enter coordinate"))
x_2 = float(input("Enter coordinate"))
y_1 = float(input("Enter coordinate"))
y_2 = float(input("Enter coordinate"))

a = (x_1, x_2)
b = (y_1, y_2)


d = math.dist(a,b)
print("The distance between the two coordinates is", d)

def make_change(amount):
    '''Item 6.
    Make Change. 5 points.

    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.

    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.

    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line
amount = float(input("Enter numerical grade: "))
diffChange = amount
countPeso = 0
count25 = 0
count10 = 0
count05 = 0
count01 = 0
if amount == 0:
    return 0
while diffChange >= 1 :
    countPeso += 1
    diffChange -= 1
while diffChange >= .25 :
    count25 += 1
    diffChange -= .25
while diffChange >= .10 :
    count10 += 1
    diffChange -= .10
while diffChange >= .05 :
    count05 += 1
    diffChange -= .05
while diffChange >= .01 :
    count01 += 1
    diffChange -= .01

print(("The change for" amount "is" f"1P:{countPeso}/25C:{count25}/10C:{count10}/5C:{count05}/1C:{count01}"))
