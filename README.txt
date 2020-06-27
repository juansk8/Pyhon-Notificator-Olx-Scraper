**Disclaimer**
Remenber do web scraping can be hurtful to the web sites because we'r doing request to servers and if we dont consider that can overload them and event get banned for ip. so is important dont scrap to high frecuency, in this case the frecuency of getting data is randomized between 20min and 40min.

**Scareper***
This app scrap a single page from a popular latin america web site call Olx.com, is similar to ebay. the data got by spider is storage and replace in a txt file and aditionaly it notificates to you by sending a message to your email if some condition on data are true.

This only collect information about price and title of annoucement. You can add another information tweaking a litte the Spider function.

You can or should:

-install the selenium and pandas libraries.

-add the email addresses (remitter and receiver) of messageNotification function on Scraper_Olx.py. And change also the smtp email server domain if you use another instead of gmail.com

-modify the url variable on Spider function to scrap the items that you want on olx.

-change the bound of 3 cycles "range(3)" on the first "for" in Spider function. this parameter allow control the amount of data that you want to scrap and storage per each cycle on main execution. 

