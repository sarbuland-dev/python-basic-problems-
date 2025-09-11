def access(user):
    match user:
        case "Admin"|"Manager":
        # case _ if   "Admin"   in user or "Manager" in user:
            return("Full Access!")
        case _ if  "Guest" in user:
            return("Limited Access!")
        case _:
            return("No Access!")

n=input("Enter your post ").capitalize().strip()
print(access(n))