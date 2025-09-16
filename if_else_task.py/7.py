while True:
    try:
        x = input("Enter your string: ").lower()
        vowels = ["a", "e", "i", "o", "u"]

        count = 0
        for i in x:
            if i in vowels:   
                count += 1

        print(f"Total vowels: {count}")

    except:
        print("Enter a valid string")
