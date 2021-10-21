# A basic interpreter to add functions to systemf brainfuck
# Python 3.8

file = input("Input file to be interpreted\n")
with open(file, 'r+') as f:
  functions = []
  y = 1
  lines = f.read().replace(" ", "").replace("\n", "").replace("\t", "").split(";")
  file_string = ""
  for i in lines:
    if i.startswith("$"):
      if len(i.split("|")) == 2: #makes sure it isn't just a function call
        functions.append([i.split("|")[0], i.split("|")[1], y]) # store lines number for possible future debug purposes
        y += 1
      else:
        file_string+=i
        y += 1
        continue
    else:
      file_string+=i
      y += 1
      continue

  for x in functions:
    file_string = file_string.replace(x[0], x[1])

print("\nOUTPUT:\n\t" + file_string)
    
#Example Code

# $function_name | >+++++++++[<++++++++>-]<.      prints ASCII value for H (line does not execute until called.)
#
# $function_name                                   calls function to print 
