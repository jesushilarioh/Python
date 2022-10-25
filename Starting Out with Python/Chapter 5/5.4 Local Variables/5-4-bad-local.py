
def main():
    get_name()
    print('Hello', name) #This causes an error!

def get_name():
    name = input('Enter your name: ')

main()

