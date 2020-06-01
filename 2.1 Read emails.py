import imapclient
conn= imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('zoe9955@gmail.com','xwjymwahtvswmxbm')
conn.select_folder('INBOX',readonly=True)
UIDs= conn.search('SINCE 31-MAY-2020') # Returns indexes of mails since may 31st
# print(UIDs)
raw_msg= conn.fetch([8816],['BODY[]','FLAGS']) # The mail indexes should be in a list
print(raw_msg) # Still need to clean up the data
print(conn.list_folders())
conn.select_folder('INBOX',readonly=False)
conn.delete_messages([8815]) # deletes emails


import pyzmail # Use this to clean up
message= pyzmail.PyzMessage.factory(raw_msg[8816][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from')) # from
print(message.text_part.get_payload().decode('UTF-8')) # to get the body
# if there is html, use html_part

