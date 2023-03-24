def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    with open(file_name) as file:
        list = [i.split() for i in file if len(i) > 0 and i.startswith('From ')]
        countlist = [i[2] for i in list]
        my_dic = {i:countlist.count(i) for i in countlist}
        print(my_dic)

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
