actual_code="Money:3"
code=str(input("Type password:"))
password_attempts=1

while code!=actual_code:
    print("try again bro")
    password_attempts+=1
    code=str(input("Type password:"))
    if password_attempts==5:
        print("damn bro, you are out of attempts")
        break

if code==actual_code:
    print("Good boy or something")
    