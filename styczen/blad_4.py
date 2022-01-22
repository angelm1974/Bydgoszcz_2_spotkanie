from time import sleep
sekunda=0

while True:
    try:
        print(sekunda)
        sekunda+=1
        sleep(1)
    except KeyboardInterrupt:
        print("Nie rób tak!!!")