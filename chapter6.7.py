def triangle():
    ch = ''
    while ch!= 'x':
        for i in range(1,7):
            ch = input('enter x, else continue')
            if ch!= 'x':
                for j in range(0,i):
                    print("*", end="")
                print("")
            else:
                break

triangle()

# def triangle():
#     for i in range(7):
#         ch = input('enter x, else continue')
#         if ch!= 'x':
#             for j in range(i):
#                 print("*", end="")
#             print("")

# triangle()
# ch = input('enter x, else continue')
# while ch!= "x":
#     triangle()
#     ch = input("enter x, else continue")