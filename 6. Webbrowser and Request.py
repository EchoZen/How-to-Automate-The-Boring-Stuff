import webbrowser, sys, pyperclip, requests
# webbrowser lets you open a webpage
# webbrowser.open('https://www.youtube.com/')

# requests module lets you download webpages and files
# Not very good if you have to login to website first

# requests.get() returns a Response object.
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code) # 200 means okay

# The raise_for_status() Response method will raise an exception if the download failed
# Use it to to stop program immediately if download fails
res.raise_for_status()

# print(len(res.text))
# print(res.text[:500])

# You can save a downloaded file to your hard drive with calls to the iter_content() method.
playFile= open('RomeoAndJuliet.txt','wb')
# Have to include write binary to include unicode characters, even for plain text doc

for chunk in res.iter_content(100000): # Number of bytes per chunk
    playFile.write(chunk)

playFile.close()


