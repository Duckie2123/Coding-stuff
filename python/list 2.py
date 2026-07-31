actual_code="I hate jews"
code=str(input("Type password:"))
password_attempts=1

while code!=actual_code:
    print("try again bro")
    password_attempts+=1
    code=str(input("Type password:"))
    if password_attempts==5:
        print("fuck you")
        break

if code==actual_code:
    print("Good jew")
    