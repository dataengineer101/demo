filename = r"C:\Users\mark\PycharmProjects\demo_new\data.csv"
with open(filename) as file_object:
   for line in file_object:
    # print(line)
    # print(line.strip('\n'))
    # print(line.split(","))
    # print(line.strip().split(","))

    # line = line.replace(',\n', '')
    # print(line)

    x = line.splitlines()
    # x = line.replace('\r\n', '')
    # x = x.replace("\r", "")
    # x = x.replace("\n", "")

    print(x)

    This is new code here

ghghgfgh fffggddd

fggf
