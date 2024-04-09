# =======================================================================
# Project: Animal conservation web scraper
# Description: Cleaning and visualizing collected data.
# The project uses regular expressions to clean unwanted html code from web scraper data collected on animal classes and conservation status. The dataset (a JSON file) is narrowed down to include fewer animal classes and conservation statuses and then stored in a Pandas dataframe. The Statsmodels library is used to visualize the smaller dataset in a mosaic plot.
# Background: Coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

# ==== *** ====

# The main.py file contains code that:
# - uses regular expressions to identify and collect unwanted html code in the dataset.
# - loops through the (large) dataset to extract data for a smaller dataset.
# - customizes the mosaic plot's colors and font sizes.
# - stores the dataset in a Pandas dataframe for use with the mosaic plot.
# - uses Statsmodels' mosaic() function to create a mosaic plot.
# =======================================================================

import json
import re
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

# Opens json file:
with open("data.json", "r") as text:
  data = json.load(text)

# Removes specified (html) string pattern from the data's "Category" key:
# - compile() identifies and collects unwanted data
for item in data:
  item["Category"] = re.compile(" [\.(]").split(item["Category"])[0]

### Narrows the json dataset to include fewer classes and conservation statuses:

classes = ["Mammalia", "Aves", "Reptilia"]
statuses = ["Endangered", "Critically endangered", "Vulnerable"]

# Extracts and stores data on animals in dataset that match the values in both 'classes' and 'statuses' variables:
mosaic_data = []
for item in data:
  if item["Animal Class"] in classes and item["Category"] in statuses:
    mosaic_data.append(item)

### Customizes the mosaic plot:

# Sets new column colors of the mosaic plot:
properties = {
    "Endangered": {
        "color": "#FACDB6"
    },
    "Critically endangered": {
        "color": "#C5CADE"
    },
    "Vulnerable": {
        "color": "#A8DBD2"
    },
}

# Sets new font size for cell and axes labels:
plt.rc("font", size=8)

# Creates pandas dataframe with the extracted data from the mosaic_data list:
mosaic_dataframe = pd.DataFrame(mosaic_data)

# Creates the mosaic plot using the mosaic() function:
fig = mosaic(
    mosaic_dataframe,
    ["Category", "Animal Class"],
    title="Conservation Status by Animal Class",
    gap=[0.02, 0.02],
    axes_label=True,
    properties=lambda x: properties[x[0]],
)

plt.savefig("animal_conservation_status.png")
