import os
# run something on all the files. Can delete or move or copy, anything!
os.chdir(r'C:\Users\zchen\OneDrive\Documents\Python stuff')
for foldername, subfolders, filenames in os.walk('Shopee'):
    print('Folder name: '+ str(foldername))
    print('Sub-folder names in '+ str(foldername) +' are '+ str(subfolders))
    print('File names in '+ str(foldername) +' are '+str(filenames))