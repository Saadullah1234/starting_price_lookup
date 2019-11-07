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
