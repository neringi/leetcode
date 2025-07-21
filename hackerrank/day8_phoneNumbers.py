# HackerRank Day 8
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input().strip())
    phoneBook = {}

    for i in range(0, n):
        name, phoneNumber = input().split(" ")
        phoneBook[name] = phoneNumber
        
    while True:
        try:
            name = input()

            if name in phoneBook:
                print('{}={}'.format(name, phoneBook[name]))
            else:
                print('Not found')
        except:
            break