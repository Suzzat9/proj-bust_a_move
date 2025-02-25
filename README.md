# Team Bust-a-Move! Exploring Regional Mobility in the United States

This is a project I worked on with two other classmates, on visualizing regional mobility in the US during the covid-19 pandemic. The proj-paper file has more details on our scope and methodology. I worked on the dash application portion of this project and part of the data cleaning/munging process. 

## How to Install
We have included an install.sh and requirements.txt file for the user to create a virtual environment and download the required packages. After doing this, run $ python3 app.py in the terminal. The user will then be directed to a web address that runs the application.

If you would like to call the API and clean the data, navigate to the data folder and enter "$ python3 clean_data.py" in the command line. Relevant print statements will appear as the functions are called. 

## How to Interact
This chloropleth map is color coded based on housing price changes, and there are a series of graphs on the right that present data for a specific county in the map. The chloropleth map can show the entire US on one color scale if the “Full Map” radio button is selected, or it will highlight counties that we’ve determined to be high risk if “High Risk” is selected. By hovering over a county, the user can see general data on each county, which can help guide the user to click on counties that they find interesting. When a user clicks on a county on the map, the graphics on the right will change to reflect the characteristics of that county. The user can choose to view different characteristics by selecting different categories in the dropdown. 

### Interesting Examples:
Take a look at some of the counties in Arizona and Idaho that have seen a steep increase in housing prices, and also have relatively low median incomes and high poverty rates. 
