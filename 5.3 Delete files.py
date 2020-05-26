import os

# IMPORTANT! Delete is permanent! Do a dry run first
# Delete a file
os.chdir(r'C:\Users\zchen\OneDrive\Documents\Python stuff\Shopee')
# os.unlink(r'Spaghetti\subwaymeatball.txt')

# Delete an EMPTY folder
# os.rmdir(r'Spaghetti')

# Delete non-empty folder
# import shutil
# shutil.rmtree('Spaghetti_backup')

for filename in os.listdir():
    if filename.endswith('txt'):
        # os.unlink(filename)
        print(filename) # Dry run so you don't delete accidentally

# send2trash 3rd party module sends files to recycling bin