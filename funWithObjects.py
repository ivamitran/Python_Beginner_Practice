# the syntax of dictionary objects in Python, not exactly the same as class objects
object = {
    "object1": "object1",
    "object2": "object2",
    "object3": "object3",
}
print(object.get("object1"))

# creates a user object which stores a user's username and password
# name
def createUser(name, username, password):
    userName = username
    passWord = password
    # name below doesn't represent the parameter I think
    name = {
        "username": userName,
        "password": passWord,
    }
    return name


list1 = []
input1 = input("What is your name: ")
input2 = input("What is your username: ")
input3 = input("What is your password: ")
list1.append(createUser(input1, input2, input3))
# print(Ivan.get("username")) ERROR, 'Ivan' is not defined, as you can see, there are some limitations when it comes to creating objects with function returns
