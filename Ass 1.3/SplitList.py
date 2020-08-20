fname = input("Enter file name : ") #input filename by User. 
fh = open(f"F:\\uni\RKU\\5th Sem\Python Programming II - CE523\ASS Py Files\{fname}")             #fh=file handler.
lst = []                     #creates an empty list constructor.
for line in fh:
   line.rstrip()             #strips all unnecessary spaces.
   words = line.split()      #splits the string in variable 'line' into a list of words.
   for element in words:     #2nd loop (nested) - goes through each element of 'words' list.
      if element not in lst: #if statement checks if elements are not in 'lst' (i.e. the list constructor).
         lst.append(element) #adds all the elements not in lst throughout the iterations.
         lst.sort()          #sorts the elements in 'lst'.
print(lst)