def do_stuff(t):
    s = tuple(t)
    x = set()
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            x.add(t[index:index+size])
    return x

def main():
    s = raw_input()
    print do_stuff(s)

main()