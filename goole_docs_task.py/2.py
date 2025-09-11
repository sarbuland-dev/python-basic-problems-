# def greeting(details):
#     match details:
#         case [time, name]:
#             return f"Good {time} {name}"
#         case [time, *names] if len(names) > 1:
#           for i in names:
#             print  (f"Good {time} {i}!")                     
#         case _:
#             return "Something went wrong"



# print(greeting(["Morning", "ali khan"]))
# print(greeting(["Afternoon", "sara"]))
# print(greeting(["Evening", "hassan", "bilal", "ahmad"]))













def my_func():
    x = 10  # local variable
    print("Inside function:", x)

my_func()
print(x)  #  Error: x is not defined
