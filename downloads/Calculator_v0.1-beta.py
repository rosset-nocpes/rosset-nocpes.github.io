import sys

print(sys.version)
print('Two-action calc. v0.1-beta')
print('Welcome to two-action calculator!')

while True:
    val1 = input("Enter first number: ")
    val2 = input("Enter second number: ")
    val3 = input("Enter third number: ")
    print("Choose first action:")
    print("1. + \n2. - \n3. * \n4. / \n5. Exit")
    answer = input("Enter number of first action: ")
    print("Choose second action:")
    print("1. + \n2. - \n3. * \n4. / \n5. Exit")
    answer2 = input("Enter number of second action: ")
    if answer == '1' and answer2 == '1':
        res = int(val1)+int(val2)+int(val3)
        print(val1 + " + " + val2 + " + " + val3 + " = " + str(res))
    elif answer == '1' and answer2 == '2':
        res = int(val1)+int(val2)-int(val3)
        print(val1 + " + " + val2 + " - " + val3 + " = " + str(res))
    elif answer == '1' and answer2 == '3':
        res = int(val1)+int(val2)*int(val3)
        print(val1 + " + " + val2 + " * " + val3 + " = " + str(res))
    elif answer == '1' and answer2 == '4':
        if val3 == '0':
            print('''Don't divise 0''')
        else:
            res = int(val1)+int(val2)/int(val3)
            print(val1 + " + " + val2 + " / " + val3 + " = " + str(res))
    elif answer == '2' and answer2 == '1':
        res = int(val1)-int(val2)+int(val3)
        print(val1 + " - " + val2 + " + " + val3 + " = " + str(res))
    elif answer == '2' and answer2 == '2':
        res = int(val1)-int(val2)-int(val3)
        print(val1 + " - " + val2 + " - " + val3 + " = " + str(res))
    elif answer == '2' and answer2 == '3':
        res = int(val1)-int(val2)*int(val3)
        print(val1 + " - " + val2 + " * " + val3 + " = " + str(res))
    elif answer == '2' and answer2 == '4':
        if val3 == '0':
            print('''Don't divise 0''')
        else:
            res = int(val1)-int(val2)/int(val3)
            print(val1 + " - " + val2 + " / " + val3 + " = " + str(res))
    elif answer == '3' and answer2 == '1':
        res = int(val1)*int(val2)+int(val3)
        print(val1 + " * " + val2 + " + " + val3 + " = " + str(res))
    elif answer == '3' and answer2 == '2':
        res = int(val1)*int(val2)-int(val3)
        print(val1 + " * " + val2 + " - " + val3 + " = " + str(res))
    elif answer == '3' and answer2 == '3':
        res = int(val1)*int(val2)*int(val3)
        print(val1 + " * " + val2 + " * " + val3 + " = " + str(res))
    elif answer == '3' and answer2 == '4':
        if val3 == '0':
            print('''Don't divise 0''')
        else:
            res = int(val1)*int(val2)/int(val3)
            print(val1 + " * " + val2 + " / " + val3 + " = " + str(res))
    elif answer == '4' and answer2 == '1':
        if val2 == '0':
            print('''Don't divise 0''')
        else:
            res = int(val1)/int(val2)+int(val3)
            print(val1 + " / " + val2 + " + " + val3 + " = " + str(res))
    elif answer == '4' and answer2 == '2':
        if val2 == '0':
            print('''Don't divise 0''')
        else:
            res = int(val1)/int(val2)-int(val3)
            print(val1 + " / " + val2 + " - " + val3 + " = " + str(res))
    elif answer == '4' and answer2 == '3':
        if val2 == '0':
            print('''Don't divise 0''')
        else:
            res = int(val1)/int(val2)*int(val3)
            print(val1 + " / " + val2 + " * " + val3 + " = " + str(res))
    elif answer == '4' and answer2 == '4':
        if val2 == '0' and val3 == '0' or val2 == '0' or val3 == '0':
            print('''Don't divise 0''')
        else:
            res = int(val1)/int(val2)/int(val3)
            print(val1 + " / " + val2 + " / " + val3 + " = " + str(res))
    elif answer == '5' or answer2 == '5':
        print('Thanks for using program.')
        print('Made by CoderPY4')
        break
