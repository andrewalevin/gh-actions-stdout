from datetime import datetime
from time import sleep


def main():
    while True:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print('🔷', t)
        sleep(1)

if __name__ == "__main__":
    main()