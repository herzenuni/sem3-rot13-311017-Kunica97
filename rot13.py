def rot13(s):
    result = ""

    for v in s:
        c = ord(v)

        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        result += chr(c)
    return result


def rot13_file(file_name):
    try:
        file = open(file_name, 'r')
    except:
        print("File opening error")
        return

    try:
        data = file.read()
    except:
        print("File reading error")
        return
    finally:
        file.close()

    file = open(file_name, 'w')

    try:
        file.write(rot13(data))
    except:
        print("File writing error")
        return
    finally:
        file.close()

    print("File encrypted")


if __name__ == "__main__":

    menu = """
    1. console input
    2. file input
    3. exit
    set: 
    """
    while True:
        while True:
            try:
                choice = int(input(menu))
                if choice == 1 or choice == 2 or choice == 3:
                    break
            except:
                print("input error...")

        if choice == 1:
            print("result :", rot13(input("put your string here :")))
        elif choice == 2:
            rot13_file(input("put here file path :"))
        elif choice == 3:
            break
