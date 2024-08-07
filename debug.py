def sayhi():
    print('hi')
    saybye()
def saybye():
    print('bye')
    
for i in range(5):
    print('start')
    print(i)
    sayhi()
    print('end')
