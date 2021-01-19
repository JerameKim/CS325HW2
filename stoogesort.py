def open_file(filename):
    # list of each line with numbers
    numbers_list = []
    # Read each line from data.txt and add to numbers_list as list of ints
    with open(filename, 'r') as reader:
        line = reader.readline()
        while line != '':
            numbers = []

            # make list from values in line
            numbers = line.split()

            # cast list values from string to int
            numbers = [int(i) for i in numbers]
            # calculate our own length so just get rid of the length
            numbers.pop(0)

            numbers_list.append(numbers)

            # move to the next line
            line = reader.readline()
    return numbers_list

def stoogesort(arr, low = None, high = None): 
    if high == None: 
        high = len(arr) - 1
        low = 0 

    if low >= high: 
        return

    # swap if lower value is greater than higher value
    if arr[low] > arr[high]:
        temp = arr[low] 
        arr[low] = arr[high]
        arr[high] = temp 

    if (high-low +1) > 2: 

        # one third of array
        third = (high-low + 1)//3

        # first two third 
        stoogesort(arr, low, high-third)

        # second two third 
        stoogesort(arr, low+third, high)

        # first two third again
        stoogesort(arr, low, high-third)


def write_results(filename, sorted_numbers_list):
    # open file to write to
    with open(filename, 'w') as writer:
        # get each list from list of all the lines
        for number_list in sorted_numbers_list:

            # Write to file
            for num in number_list:
                writer.write(f"{num} ")

            writer.write("\n")

if __name__ == "__main__":
    read_file = "data.txt"
    write_file = "stooge.out"

    data = open_file(read_file)

    for my_list in data:
        stoogesort(my_list)

    write_results(write_file, data)
