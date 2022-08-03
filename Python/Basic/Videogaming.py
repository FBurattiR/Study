import random


def run():
    funny_numero = random.randint(1, 100)
    cringe_numero = int(input("Choose a size from 1 to 100: "))
    hp = 6
    while cringe_numero != funny_numero:
        if cringe_numero < funny_numero:
            print("Too small")
            cringe_numero = int(input("Choose a bigger cock: "))
            hp -= 1
            if hp == 0 and cringe_numero != funny_numero:
                print("Lost cock privileges")
                break
        elif cringe_numero > funny_numero:
            print("Nice cock, too long tho")
            cringe_numero = int(input("N E W  N U M B E R : "))
            hp -= 1
            if hp == 0 and cringe_numero != funny_numero:
                print("Irresponsable use of cockerTM")
                break
    print("BASED POGGERS POOTIS 2 ENJOYER NICE COCK PERFECT SIZE 10/10 you win get out please laugh im extremely sad i need something")


if __name__ == "__main__":
    run()