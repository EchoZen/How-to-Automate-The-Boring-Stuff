import shutil, os

# Copy file
# 1st argument: file to be copied
# 2nd argument: location of where the file is to be pasted
# Can also rename the file at the same time by changing 2nd argument filename
os.chdir(r'C:\Users\zchen\OneDrive\Documents')
shutil.copy(r'Spaghetti\meatball.txt',r'Spaghetti\subwaymeatball1.txt')

# Copy folder
# shutil.copytree(r'Spaghetti', r'Spaghetti_backup')

# Move file
os.chdir(r'C:\Users\zchen\OneDrive\Documents')
shutil.move(r'Spaghetti\subwaymeatball1.txt',r'Spaghetti_backup')
# Can rename by using move but move it to the same destination