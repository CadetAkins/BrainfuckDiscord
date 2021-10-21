# A basic interpreter to add functions to systemf brainfuck
# Python 3.8

file = input()
with open(file, 'r+') as f:
  functions = []
  i = 0
  lines = f.read().replace(" ", "").replace("\n", "").replace("\t", "").split(";")
  for i in lines: 
    if i.startswith("$"):
      if len(i.split) > 1: #makes sure it isn't just a function call
        functions.append([i.split("|")[0], i.split("|")[1]], i) # store lines number for possible future debug purposes
        lines.remove(i)
        i += 1
      else:
        i += 1
        continue
    else:
      i += 1
      continue
      
      
 with open(file, 'r+') as f:
  file_string = f.read()
  for x in functions:
    file_string.replace(x[0], x[1])
    
   
      

#Example Code

# $function_name | >+++++++++[<++++++++>-]<.      prints ASCII value for H (line does not execute until called.)
#
#$function_name                                   calls function to print 
