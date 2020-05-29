from selenium import webdriver

chromedriver= r'C:\Users\zchen\OneDrive\Documents\chromedriver'
browser= webdriver.Chrome(chromedriver)
link= 'https://www.google.com/'
inspectcss='#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
browser.get(link)
# Type something into search box
search_elem= browser.find_element_by_css_selector(inspectcss)
search_elem.send_keys('Rubber Ducky')
search_elem.submit()

# The following can be used too
# elem= browser.find_element_by_css_selector('')
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()
# So much more you can do with selenium module!!!