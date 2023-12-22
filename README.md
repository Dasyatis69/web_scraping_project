# web_scraping_project
Classification of Paris' hotel based on geographical location and star rating in python

Goal : 
The project was created to see if there was a corelation between geographical location and star rating. It would allow us the assert which area of Paris is best suited to look for a hotel.

Librairies used : 
- Folium to create and display the map
- Nominatim to translate scraped adresses into geographical coordinates for Folium
- Scikit-learn for the KMeans algorithme that classify the hotels
- Matplotlib.pyplot to plot the intertia graph that allowed us to choose the number of cluster

Warning : 
This code use a json file containing the hotels as input ("table_info_hotels.json") which is not present in this repository. Neither is the actual scraping code that use the Selenium librairy, code which will need to change anyway since the site where we scraped our hotels change its structure as time passes (it probably is done to prevent this type of scraping, at least I think that's part of the reason). 
