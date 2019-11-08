# Starting Price Lookup

At Bell, our sales department receives thousands of calls per day from customers inquiring about the starting prices of our smartphones. One of the sales directors is very hip and loves vintage things, especially vintage graphic cards! Everyone in the department must use new computers with weak graphic cards that cannot load most of today's graphic intensive websites.

To help our sales people get information quickly to serve our customers more efficiently, we need to create a program that spits out starting prices for a given phone in a CLI (Command-line interface).

## Technology

Below is a list of technology to use:

- You can use any programming language, we recommend: Ruby, Python, or Java
- You can use any environment, we recommend a linux environment
- Selenium WebDriver
- A driver like chromedriver (chrome) or geckodriver (firefox)

## Expectations

- When a user starts the program, the user should get a welcome message
- The program should then go to the [Bell Smartphone page](https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices) and retrieve the names of the top 12 devices
- The program should then give the user a list of these 12 devices that the user can choose 
- When a device is selected, Selenium should run in the background to visit the same [webpage](https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices) , click on the requested device, and get the starting prices for all terms listed
- Once the price is obtained, it should print the devices's name, the prices, and their respective terms to the command-line

## Things to keep in mind

- You should build the CLI so that it allows the sales staff to find the price efficiently
- How you make the CLI user-friendly is entirely up to you
- Make sure you have a detailed README with instructions on how to run your program

## How to manage your work

- Create a fork of this repo
- Make sure the repo is set to **private** and add me to the repo `jbhandari`
- Make sure to commit your code in logical portions
  - ex: `Added ability to fetch price`

## Additional Information

- Should you need any further clarifications please do not hesitate to contact me via email at `jatin.bhandari@bell.ca`
- Once the deadline has been reached (set by the hiring manager), the repo will be cloned and then analyzed privately
