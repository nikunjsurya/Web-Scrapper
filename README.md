# Web-Scrapper
This script is a web scraper designed to extract Amazon job listings from the company's job portal and send an email notification to a specified email address 
if there is an available job in a desired location. The script uses the Requests library to send a GET request to the Amazon job portal, and the Beautiful Soup 
library to parse the HTML content of the response. The script then searches the parsed HTML content for job listings that meet the specified criteria, extracts 
the job title, location, and job link from the listing, and sends an email to the specified recipient with this information. The script uses the Schedule library 
to schedule the job to run at specific intervals (e.g., every 15 minutes), and will continue running indefinitely until stopped.
