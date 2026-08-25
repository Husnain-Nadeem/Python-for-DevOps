name= "Khizar"
def greet():
    print("Hello, " + name + "!")

greet()

def local_variable():
    local_name = "Ali"
    print("Hello, " + local_name + "!")

local_variable()

### Variable Naming Conventions and Best Practices:
## /*
# It's important to follow naming conventions and best practices for variables to write clean and maintainable code:
#
# - Variable names should be descriptive and indicate their purpose.
# - Use lowercase letters and separate words with underscores (snake_case) for variable names.
# - Avoid using reserved words (keywords) for variable names.
# - Choose meaningful names for variables.
#
# #### Example:
#
# ```python
# # Good variable naming
# user_name = "John"
# total_items = 42
#
# # Avoid using reserved words
# class = "Python"  # Not recommended
#
# # Use meaningful names
# a = 10  # Less clear
# num_of_students = 10  # More descriptive
# ```
#
# ### Practice Exercises and Examples:
#
# #### Example: Using Variables to Store and Manipulate Configuration Data in a DevOps Context
#
# In a DevOps context, you often need to manage configuration data for various services or environments. Variables are essential for this purpose. Let's consider a scenario where we need to store and manipulate configuration data for a web server.
#
# ```python
# # Define configuration variables for a web server
# server_name = "my_server"
# port = 80
# is_https_enabled = True
# max_connections = 1000
#
# # Print the configuration
# print(f"Server Name: {server_name}")
# print(f"Port: {port}")
# print(f"HTTPS Enabled: {is_https_enabled}")
# print(f"Max Connections: {max_connections}")
#
# # Update configuration values
# port = 443
# is_https_enabled = False
#
# # Print the updated configuration
# print(f"Updated Port: {port}")
# print(f"Updated HTTPS Enabled: {is_https_enabled}")
# ```
#
# In this example, we use variables to store and manipulate configuration data for a web server. This allows us to easily update and manage the server's configuration in a DevOps context.

