import time

def salary():
    start = time.time()
    user_in = int(input("Enter the number of days: "))
    init = 0.01
    sum = 0.00
    print("Days     Salary")
    print("----------------------------------")
    for i in range(1, user_in+1):
        print(f"{i}     ${init}")
        sum += init
        init *= 2
    print(f"The total salary for {user_in} days is: {sum}")
    end = time.time()
    print(f"Time taken: {(end-start)*1000}")

salary()






