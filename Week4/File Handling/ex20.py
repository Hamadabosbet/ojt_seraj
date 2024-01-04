



def print_file(filename,lines_number):
    readf=open(filename,"r")
    for i in range(1,lines_number):
        line = readf.readline().strip().split(",")
        print(i, "  " ,line[-2])


def calculate_powers(number):
    return [number**i for i in range(1, 5)]

def write_to_file(filename, data):
        power_file=open(filename,"w")
        for line in data:
            power_file.write(','.join(map(str, line)) + '\n')

def main():
    start = 1
    end = 1000-1

    powers_list = []

    for num in range(start, end ):
        powers = calculate_powers(num)
        powers_list.append(powers)

    write_to_file('powers.txt', powers_list)
    print_file("powers.txt",100)

if __name__ == "__main__":
    main()






