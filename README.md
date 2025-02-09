# Starting Price Lookup

When a user starts the program, the user gets a welcome message. The program then goes to the Bell Smartphone homepage and retrieve the names of the top 12 devices. The program then gives the user a list of these 12 devices that the user can choose. When a device is selected, Selenium runs in the background to visit the same web page, clicks on the requested device, then under Pricing and device options it clicks on pay a subsidized phone price and gets the starting prices for all terms listed. Once the price is obtained, it prints the devices's name, the prices, and their respective terms to the command-line.

## Instructions to run the project (Linux/MacOS)

1) Clone the project from GitHub

2) Download chromedriver (Chrome) or geckodriver (Firefox) from their respective websites

3) Place the executable file of the web driver in the project directory

4) Open Terminal

5) Go to the project directory

6) To install Selenium Webdrvier, type

```
pip install selenium
```

7) Now, to run the program, type 

```
python scraper.py
```

8) After execution, you will see the a welcome message, after which the Bell Smartphone Homepage will load in the foreground

9) After the products have been printed on the CLI, the user can make a selection by typing the index number of the phone to select




## Instructions to run the project (Windows)

1) Clone the project from GitHub

2) Download chromedriver (Chrome) or geckodriver (Firefox) from their respective websites

3) Place the executable file of the web driver in the project directory

4) Now add the PATH of the web driver to Windows path variable

5) Right-click on My Computer > Properties > Advanced tab > Environment Variables > System Variables

6) Edit the PATH and copy paste the address of the local directory where the web driver is placed

7) Download get-pip.py to install PIP

8) Open Command Prompt

9) To install PIP, type

```bash
python get-pip.py
```

10) To install Selenium, type

```bash
pip install selenium
```

11) Now go to the project directory via the command prompt

12) Now, to run the program, type 

```bash
python scraper.py
```

13) After execution, you will see the a welcome message, after which the Bell Smartphone Homepage will load in the foreground

14) After the products have been printed on the CLI, the user can make a selection by typing the index number of the phone to select