



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


  def getAge(self):

    if self.age <= 1:
      age="The person is an infant."
    # if a person is older than 1 but younger than 13
    elif self.age > 1 and self.age < 13:
      age="The person is a child."


    # if a person is at least 13, but less than 20
    elif self.age >= 13 and self.age < 20:
      old = "The person is a teenager."


    elif  self.age >= 20:
      age = "The person is an adult."
    else:
      age = "Check that your input is an integer and try again."

    return  age
