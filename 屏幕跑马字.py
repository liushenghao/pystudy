import os
import time

def main():
    content = 'hello world\n'
    while True :
        os.system('cls')
        print(content)
        time.sleep(0.01)
        content = content[1:]+content[0]

if __name__ == "__main__":
    main()