import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_str) -> int:                          #the vowel_count function return the number of vowels in an inputted string.
                                                            #Input: (type: str). the function will count the vowels. Output: integer, the number of vowels in the input string.
   vowels = "aeiouAEIOU"                                    #The parameter input_str is of type str. The return type is int.
   return sum (1 for char in input_str if char in vowels)

# Part 2
def short_lists(input_list: list[list[int]]) -> list[list[int]]:   #The function short_lists returns a new list consisting of those elements of the input list (in the same order) that are of length 2.
                                                                   #Input: input_lists, a list containing nested lists of integers. Output: A list containing only the sub lists from input_list that have exactly 2 elements
    return [lst for lst in input_list if len(lst) == 2]            #parameters: input_list, a list containing sub lists of integers. Return type: A list of sub lists, where each sublist has two integers.

# Part 3
def ascending_pairs(pairs_list: list[list[int]]) -> list[list[int]]: #The function ascending_pairs purpose is to return a new list in which each sublist of length 2 is sorted from lowest to highest.
    result = []                                                      #Input: pairs_list, a list of sub lists that have integers. Output: a new list where all sub lists are ordered lowest to highest.
    for lst in pairs_list:                                           #To show that the input parameter pairs_list is a list of sub lists with integers, it is annotated as list[list[int]].
        if len(lst) == 2:                                            #The return type is list[list[int]], indicating that the function returns a list of sub lists of integers.
            result.append(sorted(lst))
        else:
            result.append(lst)
    return result

# Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

def add_prices(price1, price2):                         #the function add_prices adds two prices, and when the cents go over 99, then it converts it to a dollar. The function returns a new Price object representing the sum of the two input prices.
    total_cents = price1.cents + price2.cents           #input: price1 and price2, object with type Price with cents and dollars. Output: A new Price object gotten from total of dollars and cents from price 1 and price2
    total_dollars = price1.dollars + price2.dollars + total_cents // 100 # type annotations: function adds cents and dollars from price1 and price2. Converts over 99 cents into dollars and returns a Price object.
    total_cents = total_cents % 100
    return Price(total_dollars, total_cents)

# Part 5
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

def rectangle_area(rectangle: Rectangle) -> int:         #the function rectangle_area returns the area of a rectangle represent by top_left corner and bottom_right.
    width = rectangle.bottom_right.x - rectangle.top_left.x   #input: rectangle: object Rectangle containing the objects top_left and bottom_right. They have x and y coordinates.
                                                              #output: area of the rectangle as an int, a product of width and height.
    height = rectangle.top_left.y - rectangle.bottom_right.y  #type annotations: the rectangle's area is an int to match the return type

    return width * height


# Part 6
class Book:
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title

def books_by_author(author_name: str, books_list: list[Book]) -> list[Book]:    #the books_by_author function returns a list of books written by a certain author from a list of Book
    return [book for book in books_list if author_name in book.authors]         #input: author_name: a string with a name of the author and book_list: A list of Book objects with title and list of authors
                                                                                #output: a list of Book and author_name
                                                                                #type annotations: author_name is a str, and book_list is a list of Book. Return type: function returns a list of Book
# Part 7
class Circle:                                                           #the circle_bound returns a circle from the rectangle provided. The radius is the distance from the center to the corner of the rectangle.
    def __init__(self, center: Point, radius: float):                   #input: rectangle of type Rectangle which will be used to find the bounding circle.
        self.center = center                                            #output: Circle object. the center of circle is the center of the rectangle.
        self.radius = radius

def circle_bound(rectangle: Rectangle) -> Circle:   #type annotations:
    center_of_rectangle = rectangle.center()        #uses the center point of the rectangle
    radius_of_circle = rectangle.distance_to(rectangle.top_right) #uses center to top-right corner
    return Circle(center_of_rectangle, radius_of_circle)

# Part 8
class Employee:
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate

def below_pay_average(employees: list[Employee]) -> list[str]:  #the function below_pay_average is used to identify employees that get paid less than average among the employees on the list.
    if not employees:                                           #input: list of Employee objects with the attributes name, name of the employee and pay_rate the pay of the employee as an integer.
        return []                                               #output: list of strings with name of employees who have a below pay rate than the others in the list. If empty, then it returns an empty list.
    total_pay = sum(employee.pay_rate for employee in employees) #type annotations: list[Employee]: The function expects a list of Employee objects. list -> str: function return a list of strings with employees who get paid less than average.
    average_pay = total_pay / len(employees)

    below_average = [employee.name for employee in employees if employee.pay_rate < average_pay]

    return below_average


