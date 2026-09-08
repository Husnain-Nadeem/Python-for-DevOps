## using membership operator to check if a key exists in the dictionary or not
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
if "age" in my_dict:
    print("Key 'age' exists in the dictionary.")

if "city"  in my_dict:
    print("Key 'city' exists in the dictionary.")

if "alice" not in my_dict:
    print("Key 'alice' does not exist in the dictionary.")


a= "Hello, World!"
b= "Python is great."

if a is b:
    print("Both strings are the same object in memory.")
elif a is not b:
    print("The strings are different objects in memory.")