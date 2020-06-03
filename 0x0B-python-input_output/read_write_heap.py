from sys import argv, exit


if len(argv) != 4:
    print("Usage: {}  <pid> <String_to_Replace> <New_String>".format(argv[0]))
    exit(1)

pid = argv[1]
string = argv[2]
newString = argv[3] + "\0"


address = ""
maps_path = "/proc/" + pid + "/maps"
try:
    with open(maps_path, "r") as maps_file:
        for line in maps_file:
            if "[heap]" in line:
                if "r" not in line or "w" not in line:
                    print("  [ERROR] PID heap doesn't " +
                          "have read/write permissions")
                    exit(0)

                line = line.split()
                print("    >< pathname: {}".format(maps_path))
                print("    >< address: {}".format(line[0]))
                print("    >< permissions: {}".format(line[1]))
                print("    >< offset: {}".format(line[2]))
                print("    >< device: {}".format(line[3]))
                print("    >< inode: {}".format(line[4]))
                address = line[0].split('-')

except IOError as e:
    print("  [ERROR] cannot open file {}".format(maps_path))
    print(e)
    exit(1)

start = int(address[0], 16)
end = int(address[1], 16)

# print("  <> Searching for string {}... ".format(string), end="")
mem_path = "/proc/" + pid + "/mem"
try:
    with open(mem_path, "rb+") as mem_file:
        mem_file.seek(start)
        heap = mem_file.read(end - start)

        try:
            index = heap.index(string.encode("ASCII"))
#            print("the string has been located.")
#            print("    >< index: {}".format(index))
        except Exception as e:
            print("  [ERROR] cannot locate string {}".format(string))
            print(e)
            exit(0)

#        print("  <> Replacing string {} ".format(string), end="")
#        print("with {}... ".format(newString[:-1]), end="")
        mem_file.seek(start + index)
        mem_file.write(newString.encode("ASCII"))
#        print("the string has been replaced.")

except IOError:
    print("  [ERROR] cannot write file {}".format(mem_path))
    exit(1)

print("All Done!")
