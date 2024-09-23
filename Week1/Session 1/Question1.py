# Problem 1
def welcome():
    print("Welcome to The Hundred Acre Wood!")
# Problem 2
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
# Problem 3
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
        
# Problem 4
def get_item(items, x):
    if x > len(items):
        return None
    return items[x]

# Problem 5

def sum_honey(hunny_jars):
    total = 0
    for num in hunny_jars:
        total += num
    print(total)
    
# Problem 6
def doubled(hunny_jars):
    # for i in range(len(hunny_jars)):
    #     hunny_jars[i] = hunny_jars[i]*2
    # print(hunny_jars)
    doubled = [num*2 for num in hunny_jars]
    print(doubled)

# Problem 7

def count_less_than(race_times, threshold):
    counter = 0
    for val in race_times:
        if val < threshold:
            counter += 1
    print(counter)
    
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)
race_times = []
threshold = 4
count_less_than(race_times, threshold)