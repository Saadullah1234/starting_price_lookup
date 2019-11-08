from selenium import webdriver
from selenium.webdriver.chrome.options import Options

WINDOW_SIZE = "1600,900"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--silent")

homepage = "https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices"

########################################################################################################################################
"""
Part 2 & 3
- The program should then go to the Bell Smartphone page and retrieve the names of the top 12 devices
- The program should then give the user a list of these 12 devices that the user can choose 
- Save the selected choice (for now)
"""
product_dict = {}

# create an initial Chrome session
driver = webdriver.Chrome()
driver.get(homepage)

product_list = driver.find_element_by_class_name("rsx-product-list-wrap-outer").find_elements_by_class_name("rsx-product-list-product")

for product in product_list[:12]:
    link = product.find_element_by_class_name("rsx-product-hotspot")
    name = link.find_element_by_tag_name("h3").find_element_by_tag_name("span").text
    product_dict[name] = link

driver.close()

product_keys = list(product_dict.keys())
for i in range(0, len(product_keys)):
	print("\t{0}.\t{1}".format(i+1, product_keys[i]))

selected_choice = int(input("Select a phone from list for further details: "))
############################################################################################################################################
"""
Part 4 & 5
- When a device is selected, Selenium should run in the background to visit the same webpage , 
	click on the requested device, then under Pricing and device options click on pay a subsidized 
	phone price and get the starting prices for all terms listed
- Once the price is obtained, it should print the devices's name, the prices, and their respective terms to the command-line
"""

# start a headless chrome session so selenium runs in the background

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(homepage)

product_list = driver.find_element_by_class_name("rsx-product-list-wrap-outer").find_elements_by_class_name("rsx-product-list-product")
link = product_list[selected_choice-1].find_element_by_class_name("rsx-product-hotspot")
link.click()

radio_button = driver.find_element_by_id('pricing-options-radios').find_elements_by_class_name('rsx-label')[1]

radio_button.click()

subsidized_list = driver.find_element_by_id('bcx-order-now-group-subsidized').find_elements_by_class_name('bcx-order-now-box-body')

for element in subsidized_list:
	terms = []
	price = element.find_element_by_class_name('rsx-price').text
	term_elems = element.find_elements_by_tag_name('p')
	for term_elem in term_elems:
		terms.append(term_elem.text)
	terms = " ".join(terms)
	print("\n\nProduct details for: ", product_keys[selected_choice-1])
	print("Price: {0}\nTerms: {1}".format(price, terms))

driver.close()