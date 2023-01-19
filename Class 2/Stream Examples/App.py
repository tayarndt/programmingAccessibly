from Helpers import show_name

def main():
    result = show_name(input("Enter your name: "))
    if result == "":
        return False
    else:
        return True

if __name__ == "__main__":
    status = main()
    if status == True:  
        print("The program exited successfully")
    else:
        print("The program exited with an error")
