import keyboard
import time


def create_digraph():
    sumOfDigraph = {}
    countOfDigraph = {}
    prev = "enter"
    t = time.time_ns()
    while 1:
        key = keyboard.read_key()
        if key == "enter":
            break
        if prev != "enter":
            t = time.time_ns()
            if prev != "esc":
                if prev != key:
                    if (prev, key) in sumOfDigraph:
                        countOfDigraph[prev, key] += 1
                        sumOfDigraph[prev, key] += t - prev_time
                    else:
                        countOfDigraph[prev, key] = 1
                        sumOfDigraph[prev, key] = t - prev_time
        prev = key
        prev_time = t
    for p in sumOfDigraph:
        sumOfDigraph[p] = sumOfDigraph[p] / countOfDigraph[p]
    return sumOfDigraph


def validate(person1, person2):
    count = 0
    sum_error = 0
    for p in person1:
        if p in person2:
            sum_error = abs(person2[p] - person1[p])
            count += 1
    val = sum_error / count
    if val > 20_000_000:
        return False
    else:
        return True



def main():
    print("create person1")
    person1 = create_digraph()
    print("\n",person1)
    print("\ntype 'esc' to create another")
    keyboard.wait("esc")
    print("create person2")
    person2 = create_digraph()
    print("\n",person2)
    while True:
        print("\ntype 'esc' to check who you are")
        keyboard.wait("esc")
        print('type "hello world my name is"')
        anonymous = create_digraph()
        check1 = validate(person1, anonymous)
        check2 = validate(person2, anonymous)
        if check1:
            print("\nYou are person1")
        elif check2:
            print("\nYou are person2")
        else:
            print("Who are you ?")


if __name__ == "__main__":
    main()
