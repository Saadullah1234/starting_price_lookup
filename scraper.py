"""
Module for Starting Price lookup for Bell Mobility Devices.

The program lists out names for Bell Mobility top 12 devices
and displays prices and terms for the selected device.
"""
# Importing the necessary libraries
from time import sleep
import selenium.webdriver.support.ui as ui

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setting arguments for headless chrome
WINDOW_SIZE = "1600,900"
DRIVER_OPTIONS = Options()
DRIVER_OPTIONS.add_argument("--headless")
DRIVER_OPTIONS.add_argument("--window-size=%s" % WINDOW_SIZE)
DRIVER_OPTIONS.add_argument("--log-level=3")
DRIVER_OPTIONS.add_argument("--silent")

# Desired homepage
HOMEPAGE = "https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices"
print("\n\n\n\t\t\033[0;32;40m Welcome to the Bell"
	  " Mobility Smartphone Homepage!\n\n\n")
sleep(2)
print("\t\t Canada's Largest Telecommunication Company\n\n\n")
sleep(2)
PRODUCT_DICT = {}

# Initialize webdriver and start a session
DRIVER = webdriver.Chrome('./chromedriver')
DRIVER.get(HOMEPAGE)

# Find the required element and the contained product list
PRODUCT_LIST = DRIVER.find_element_by_class_name(
	"rsx-product-list-wrap-outer").find_elements_by_class_name(
		"rsx-product-list-product")

for product in PRODUCT_LIST[:12]:
	LINK = product.find_element_by_class_name("rsx-product-hotspot")
	name = LINK.find_element_by_tag_name("h3").find_element_by_tag_name(
		"span").text
	PRODUCT_DICT[name] = LINK

DRIVER.close()
PRODUCT_KEYS = list(PRODUCT_DICT.keys())

# Display top 12 options to the user
print("\n\nThe list below shows top 12 devices of Bell Mobility:\n\n")
for i, _ in enumerate(PRODUCT_KEYS):
	print(" {0}.\t{1}".format(i + 1, PRODUCT_KEYS[i]))
try:
	while True:
		SELECTED_CHOICE = input(
			"\n\nSelect a device from the list by entering the index number: ")
		try:
			SELECTED_CHOICE = int(SELECTED_CHOICE)
			if SELECTED_CHOICE not in range(1, len(PRODUCT_KEYS)+1):
				raise ValueError
			break
		except ValueError:
			print("\n\033[0;31;40mPlease enter a valid index number "
				  "from the list.\033[0;32;40m")

	# Start another session but in background this time (options=DRIVER_OPTIONS)
	DRIVER = webdriver.Chrome(executable_path='./chromedriver',
								options=DRIVER_OPTIONS)
	DRIVER.get(HOMEPAGE)
	WAIT = ui.WebDriverWait(DRIVER, 10)
	WAIT.until(lambda DRIVER: DRIVER.find_element_by_id(
		'deviceListWithFiltering'))
	PRODUCT_LIST = DRIVER.find_element_by_class_name(
		"rsx-product-list-wrap-outer").find_elements_by_class_name(
			"rsx-product-list-product")
	LINK = PRODUCT_LIST[SELECTED_CHOICE - 1].find_element_by_class_name(
		"rsx-product-hotspot")
	LINK.click()

	RADIO_BUTTON = DRIVER.find_element_by_id(
		"pricing-options-radios").find_elements_by_class_name(
			"rsx-label")[1]
	RADIO_BUTTON.click()
	SUBSIDIZED_LIST = DRIVER.find_element_by_id(
		"bcx-order-now-group-subsidized").find_elements_by_class_name(
			"bcx-order-now-box-body")
	print("\n\nProduct details for: ", PRODUCT_KEYS[SELECTED_CHOICE - 1])

	# Extract terms and prices from the fetched elements
	for element in SUBSIDIZED_LIST:
		terms = []
		price = element.find_element_by_class_name("rsx-price").text
		term_elements = element.find_elements_by_tag_name("p")
		for term_element in term_elements:
			terms.append(term_element.text)
		terms = " ".join(terms)
		print("Price: {0}\nTerms: {1}\n".format(price, terms))

except TimeoutException:
	print("\033[0;31;40m\nTimed out while waiting "
		  "for page to load.\n\033[0;37;40m")
except NoSuchElementException:
	print("\033[0;31;40m\n Element was not found "
		  "on page.\n\033[0;37;40m")
except Exception as error:
	print("\033[0;31;40m\nUnknown exception: {0}."
		  "\n\033[0;37;40m".format(error))
DRIVER.close()
