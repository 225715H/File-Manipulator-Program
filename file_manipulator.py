import sys
output = sys.stdout.buffer.write(b"select and input mode: reverse, copy, duplicate-contents, replace-string \n")
sys.stdout.flush()
mode = list(sys.stdin.readline().split())
contents = ""

if mode[0] == "reverce":
  if len(mode) != 3:
    print("Error: invalid input\nUsage: reverce <input_file> <output_file>")
    exit()
  with open(mode[1]) as f:
    contents = f.read()
  with open(mode[2], "w") as f:
    f.write(contents[::-1])
  print("reverce done")

elif mode[0] == "copy":
  if len(mode) != 3:
    print("Error: invalid input\nUsage: copy <input_file> <output_file>")
    exit()
  with open(mode[1]) as f:
    contents = f.read()
  with open(mode[2], "w") as f:
    f.write(contents)
  print("copy done")

elif mode[0] == "duplicate-contents":
  if len(mode) != 3 and not mode[2].isdigit():
    print("Error: invalid input\nUsage: duplicate-contents <input_file> <number_of_times>")
    exit()
  with open(mode[1]) as f:
    contents = f.read()
  with open(mode[1], "w") as f:
    for i in range(int(mode[2])):
      f.write(contents)
  print("duplicate-contents done")

elif mode[0] == "replace-string":
  if len(mode) != 3:
    print("Error: invalid input\nUsage: replace-string <input_file> <string_to_replace> <new_string>")
    exit()
  with open(mode[1]) as f:
    contents = f.read()
  with open(mode[1], "w") as f:
    f.write(contents.replace(mode[2], mode[3]))
  print("replace-string done")

else:
  print("Error: invalid mode")

