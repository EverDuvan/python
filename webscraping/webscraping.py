import mechanicalsoup 
import os

from requests.models import Response

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"

browser.open(url)
print (browser.get_url())
browser.get_current_page()
#print(browser.get_current_page())
browser.select_form()
#browser.get_current_form().print_sumary()
print(browser.get_current_form())
browser.launch_browser(url)
search_term = 'cat'
browser["q"] = search_term
browser.launch_browser()
Response = browser.submit_selected()
print ('new url:',browser.get_url)
print ('my response: \n', Response.text[:500])

new_url=browser.get_url()
browser.open(new_url)

page = browser.get_current_page()
all_images = page.find_all('img')
print (all_images)

image_sourse = []
for image in all_images:
    image = image.get('src')
    image_sourse.append(image)
print('*********************************************************************************')
print (f'img sourse: {image_sourse}')  

image
