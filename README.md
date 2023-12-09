# Edabit
8 simple OOP codes .

##First one:
 I wnt to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r) which give both 
  respective areas and perimeter (circumference).


##Second one:
  I want to Create a method in the Person class which returns how another person's age compares. Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, return a sentence in 
  the 
 following format:

  {other_person} is {older than / younger than / the same age as} me.  

##Third one:
  This time i wanna Create methods for the Calculator class that can do the following:

    Add two numbers.
    Subtract two numbers.
    Multiply two numbers.
    Divide two numbers.

##Fourth one:
    I created the instance attributes fullname and email in the Employee class. Given a person's first and last names:

    Form the fullname by simply joining the first and last name together, separated by a space.
    Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

##Fifth one:
    Create a class named User and create a way to check the number of users (number of instances) that were created, so that the value can be accessed as a class attribute.
 Examples

 u1 = User("johnsmith10")
 User.user_count ➞ 1

 u2 = User("marysue1989")
 User.user_count ➞ 2

  u3 = User("milan_rodrick")
  User.user_count ➞ 3

Make sure that the usernames are accessible via the instance attribute username.

  u1.username ➞ "johnsmith10"

  u2.username ➞ "marysue1989"

  .username ➞ "milan_rodrick"


##sixth one:
  
    Create a Book class that has two attributes:

    .title
    .author

    and two methods:

    A method named .get_title() that returns: "Title: " + the instance title.
    A method named .get_author() that returns: "Author: " + the instance author.

    and instantiate this class by creating 3 new books:

    Pride and Prejudice - Jane Austen (PP)
    Hamlet - William Shakespeare (H)
    War and Peace - Leo Tolstoy (WP)

   The name of the new instances should be PP, H, and WP, respectively.

  For instance, if I instantiated the following book using this Book class:

    Harry Potter - J.K. Rowling (HP)

  I would get the following attributes and methods:
  Examples

  HP.title ➞ "Harry Potter"
  HP.author ➞ "J.K. Rowling"
  HP.get_title() ➞ "Title: Harry Potter"
  HP.get_author() ➞ "Author: J.K. Rowling"


##seventh one:
   In the class Employee, implement the instance attributes as firstname, lastname and salary.

   Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash.
   Examples

   emp1 = Employee("Mary", "Sue", 60000)
   emp2 = Employee.from_string("John-Smith-55000")

    emp1.firstname ➞ "Mary"

   emp1.salary ➞ 60000

     emp2.firstname ➞ "John"

   emp2.salary ➞ 55000

  ##Eighth one:
     Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance should have a name and a lastname attribute plus one more attribute for each of 
      the keywords, if any.
      Examples

      john = Employee("John Doe")
      mary = Employee("Mary Major", salary=120000)
      richard = Employee("Richard Roe", salary=110000, height=178)
      giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

      john.name ➞ "John"
      mary.lastname ➞ "Major"
      richard.height ➞ 178
      giancarlo.nationality ➞ "Italian"
