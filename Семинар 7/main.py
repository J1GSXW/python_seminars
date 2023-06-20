from os.path import join, abspath, relpath, dirname, exists


main_dir = join(',')
filename = join(main_dir, "data", "data1.txt")

file = open(filename, mode="rt",encoding="utf-8")
for line in file:
    print(line)
file.close()