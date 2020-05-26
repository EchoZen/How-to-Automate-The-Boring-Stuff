import os
# returns a filepath appropriate for current operating system
print(os.path.join('folder1', 'folder2','folder3','file.png'))
print(os.sep)
# get current working directory
print(os.getcwd())
# change working directory
os.chdir(r'C:\Users')
print(os.getcwd())

# Absolute file paths always contain root folder ':C' and give complete location of program
# Relative file paths are relative to current working directory
# '.\' refers to current folder, '..\' refers to parent folder (for relative file paths)

os.chdir(r'C:\Users\zchen\PycharmProjects\How-to-Automate-The-Boring-Stuff')
print(os.path.abspath('Files.py')) # Gives you absolute path
os.chdir(r'C:\Users\zchen\OneDrive\Documents\Fungi internship\Wk1 Saccharomyces annotations')
print(os.getcwd())
print(os.path.exists('Saccharomyces_annotations_final.txt')) # Tells you if path exists in cwd
print(os.path.isfile('Saccharomyces_annotations_final.txt')) # Helps you differientiate file and folder
print(os.path.getsize('Saccharomyces_annotations_final.txt')) # gets file size in bytes
print(os.listdir(r'C:\Users\zchen\Downloads')) # Tells you whats in the cwd
os.makedirs(r'C:\Users\zchen\OneDrive\Documents\Spaghetti\Meatballs.txt') # Creates folders