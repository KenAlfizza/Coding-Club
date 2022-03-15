n = 0
while n < 5:
    print(n)
    n += 1


m = False
while m == False:
    answer = input("Please enter your age: ")
    try:
        answer = int(answer)
        m = True
    except:
        print("Answer is not a number. Please retry.")
print("Your age is ", str(answer))



contains_digit = False
s = "abc1"

for character in s:

    if character.isdigit():
        contains_digit = True

print(contains_digit)
