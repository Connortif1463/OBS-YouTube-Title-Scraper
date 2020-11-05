# OBS-YouTube-Title-Scraper
Uses a selenium browser window to detect the title from currently watching YouTube video and writes its title and link to corresponding text files. (Includes dependencies in lib folder.)

![alt text](https://raw.githubusercontent.com/Connortif1463/OBS-YouTube-Title-Scraper/master/sample%20images/screenshot_3.png)

## Installation:
- First, go here and download your os's chromedriver:
https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/
then, take that chromedriver executable and move it into the project's unzipped folder.

- Second,  install python, version 3.8.5, on your system. 
https://www.python.org/downloads/

- Third, since you'll be calling the youtube API:

  Create a project in the Google Developers Console and obtain authorization credentials so your application can submit API requests.
  https://console.developers.google.com/
  - #### From your authorization credentials, copy your API-key
  
   - After creating your project, make sure the YouTube Data API is one of the services that your application is  registered to use.

   - Go to the API Console and select the project that you just registered.
   - Visit the Enabled APIs page. In the list of APIs, make sure the status is ON for the YouTube Data API v3.

- Fourth, when you have your own api key, go to your clone folder and open key.py in notepad.
  Paste your copied API key in the quotes:
  - ##### API-KEY='YOUR_KEY_HERE' 
    and then save the file.

## Run:
Open a command line, navigate to your clone's folder and type:
python3 main.py

##### NOTE: DON'T USE THIS ON VIRTUAL MACHINES. YOUR SYSTEM IS YOUR SYSTEM AND THIS PROGRAM OFC USES YOUR MAIN OS.
