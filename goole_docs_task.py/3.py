def access(user):
    user= user.lower()
    match user:
        case "admin"|"manager":
          return("Full Access!")
        case   "guest" :
            return("Limited Access!")
        case _:
            return("No Access!")


print(access("manager"))
print(access("ADMIN"))
print(access("GUEST"))
print(access("cleaner"))