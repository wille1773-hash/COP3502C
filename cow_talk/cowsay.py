import sys
from heifer_generator import get_cows
from dragon import Dragon


def list_cows(cows):
    names = [i.get_name() for i in cows]
    print("Cows available: " + " ".join(names))


def find_cow(name, cows):
    for i in cows:
        if i.get_name() == name:
            return i
    return None


def say(cow, message):
    print(message)
    print(cow.get_image())


def main():
    cows = get_cows()
    argv = sys.argv

    if len(argv) == 1:
        print("Usage:")
        print("  python3 cowsay.py -l")
        print("  python3 cowsay.py MESSAGE")
        print("  python3 cowsay.py -n COW MESSAGE")
        return

    if argv[1] == "-l":
        list_cows(cows)
        return

    if argv[1] == "-n":
        if len(argv) < 4:
            print("Usage: python3 cowsay.py -n COW MESSAGE")
            return
        cow_name = argv[2]
        cow = find_cow(cow_name, cows)
        if cow is None:
            print(f"Could not find {cow_name} cow!")
            return
        message = " ".join(argv[3:])
        say(cow, message)
        if isinstance(cow, Dragon):
            if cow.can_breathe_fire():
                print("This dragon can breathe fire.")
            else:
                print("This dragon cannot breathe fire.")
        return

    message = " ".join(argv[1:])
    default = find_cow("heifer", cows) or cows[0]
    say(default, message)


if __name__ == "__main__":
    main()
