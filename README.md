# Animal Conservation Web Scraper: Cleaning and Vizualizing Data
Cleaning a dataset using regular expressions and visualizing the data with Python's Statsmodels library. 

## About
This project uses data collected by web scrapers from a website on the conservation status and animal class of endangered species. The data, which is stored in a JSON file, is first cleaned for unwanted HTML code using regular expressions, then narrowed down to create a smaller dataset and stored in a Pandas dataframe, and finally visualized in a mosaic plot with the Statsmodels library. 

## Project Background
The project was built as part of the coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

During this project, I practiced: 

- Using Regular Expressions to clean the data in the JSON file collected by the web scrapers. Python's 're' module and the re.compile() function were used to identify and collect unwanted HTML code in the dataset, and Python's split() function separates the useful data from the unwanted data that is not useful for display.   

- Narrowing down a large dataset, using an if statement to select a smaller number of animal classes and conservation statuses to make the data in the mosaic plot visualization easier to interpret. 

- Adding JSON data to a Pandas dataframe. 

- Using Python's Statsmodels library and its mosaic() function to create and customize a mosaic plot using the Pandas dataframe.   

## Built With 
- Python
- JSON module
- re module
- Pandas
- Statsmodels

## Launch
[See the project here.](https://replit.com/@lonemortensen/skillcrush-py-cl03-ls11-scraper-species-clean-mosaic-final#main.py)

## Acknowledgements

**Skillcrush** - I coded the project's main.py file with support and guidance from Skillcrush. 