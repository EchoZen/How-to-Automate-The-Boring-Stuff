# plain text files, readable to humans
# binary files stored in binary format. Unreadable to humans
meatball_file= open(r'C:\Users\zchen\OneDrive\Documents\Spaghetti\meatball.txt')
print(meatball_file.read())
meatball_file.close()

# Have to reopen the file to reread
meatball_file= open(r'C:\Users\zchen\OneDrive\Documents\Spaghetti\meatball.txt')
print(meatball_file.readlines()) # returns output as a list
meatball_file.close()

# Write will overwrite the file
meatball_file= open(r'C:\Users\zchen\OneDrive\Documents\Spaghetti\meatball.txt','w')
meatball_file.write('Meatball!\n') # Have to add in newline character
meatball_file.write('Meatball!\n')
meatball_file.write('Meatball!\n')

# Append adds things, does not overwrite
meatball_file= open(r'C:\Users\zchen\OneDrive\Documents\Spaghetti\meatball.txt','a')
meatball_file.write('Cheese!\n')
meatball_file.write('Cheese!\n')

# Shelf module, can store lists and dictionary, nontext data as binary file
import shelve, os
print(shelve.__file__) # Have to get rid of this module

shelfFile= shelve.open('mydata')
shelfFile['Scientists'] =['Linus Pauling', 'Marie Curie', 'George Beadle', 'Barry Marshall']
shelfFile.close()

shelfFile= shelfFile.open('mydata')
print(shelfFile['Scientists'])
shelfFile.close()

shelfFile= shelfFile.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()