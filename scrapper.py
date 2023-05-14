import requests  # Importing the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup for web scraping
import smtplib  # Importing smtplib for sending emails
from email.mime.text import MIMEText  # Importing MIMEText for creating email content
from email.mime.multipart import MIMEMultipart  # Importing MIMEMultipart for creating email structure
import schedule
import time

# Email configuration
sender_email = 'specterharvee@gmail.com'  # Sender's email address
receiver_email = 'suryanikunj@gmail.com'  # Receiver's email address
password = 'kisrcmjdcwwhtpdu'  # Password for the sender's email account
smtp_server = 'smtp.gmail.com'  # SMTP server address for Gmail
smtp_port = 587  # SMTP port number for Gmail

def send_email(subject, message):
    # Create an instance of MIMEMultipart for email structure
    msg = MIMEMultipart()
    msg['From'] = sender_email  # Set the sender's email address
    msg['To'] = receiver_email  # Set the receiver's email address
    msg['Subject'] = subject  # Set the email subject
    msg.attach(MIMEText(message, 'plain'))  # Attach the email message as plain text

    # Create an SMTP server object and connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Log in to the sender's email account
        server.send_message(msg)  # Send the email

def scrape_amazon_jobs():
    url = 'https://amazon.force.com/BBIndex'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('div', {'class': 'listing'})

    for job in job_listings:
        job_title = job.find('h6').find('a').text
        location = job.find('span').text
        job_link = job.find('h6').find('a')['href']  # Extract the URL of the job listing

        if 'Ajax' in location:
            email_subject = 'YO! You got some hiring in your desired location! GO CHECK IT OUT!!' # Set the email subject
            email_message = f"Job Title: {job_title}\nLocation: {location}\nJob Link: {job_link}"  # Set the email message
            send_email(email_subject, email_message) # Send the email
            break # Exit the loop after finding the first job

def schedule_job():
    schedule.every(15).minutes.do(scrape_amazon_jobs)

    while True:
        schedule.run_pending()
        time.sleep(1)

schedule_job()


# def scrape_amazon_jobs():
#     url = 'https://amazon.force.com/BBIndex'  # URL of the Amazon jobs page
#     response = requests.get(url)  # Send a GET request to the URL and get the response
#     soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content using BeautifulSoup

#     # Find all job listings based on the specific criteria (class = 'listing')
#     job_listings = soup.find_all('div', {'class': 'listing'})

#     for job in job_listings:
#         job_title = job.find('h6').find('a').text  # Extract the job title from the HTML structure
#         location = job.find('span').text  # Extract the location from the HTML structure

#         if 'Sidney' in location:  # Check if the location contains the desired location (Ajax)
#             email_subject = 'YO! You got some hiring in your desired location! GO CHECK IT OUT!!'  # Set the email subject
#             email_message = f"Job Title: {job_title}\nLocation: {location}"  # Set the email message
#             send_email(email_subject, email_message)  # Send the email
#             break  # Exit the loop after finding the first job

# # scrape_amazon_jobs()


# def schedule_job():
#     # Schedule the job to run every day from Friday to Monday
#     # schedule.every().friday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Fridays
#     # schedule.every().saturday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Saturdays
#     # schedule.every().sunday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Sundays
#     # schedule.every().monday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Mondays

#     schedule.every(15).minutes.do(scrape_amazon_jobs)

#     # Keep the script running indefinitely
#     while True:
#         schedule.run_pending()  # Check if there are any scheduled jobs to run
#         time.sleep(30)  # Pause the script for 30 second

# schedule_job()  # Start scheduling the job


# import win32serviceutil
# import win32service
# import win32event
# import servicemanager
# import socket
# import os
# import sys
# import requests
# from bs4 import BeautifulSoup
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import schedule
# import time

# # Email configuration
# sender_email = 'specterharvee@gmail.com'  # Sender's email address
# receiver_email = 'suryanikunj@gmail.com'  # Receiver's email address
# password = 'kisrcmjdcwwhtpdu'  # Password for the sender's email account
# smtp_server = 'smtp.gmail.com'  # SMTP server address for Gmail
# smtp_port = 587  # SMTP port number for Gmail

# def send_email(subject, message):
#     # Create an instance of MIMEMultipart for email structure
#     msg = MIMEMultipart()
#     msg['From'] = sender_email  # Set the sender's email address
#     msg['To'] = receiver_email  # Set the receiver's email address
#     msg['Subject'] = subject  # Set the email subject
#     msg.attach(MIMEText(message, 'plain'))  # Attach the email message as plain text

#     # Create an SMTP server object and connect to the SMTP server
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()  # Start TLS encryption
#         server.login(sender_email, password)  # Log in to the sender's email account
#         server.send_message(msg)  # Send the email

# def scrape_amazon_jobs():
#     url = 'https://amazon.force.com/BBIndex'  # URL of the Amazon jobs page
#     response = requests.get(url)  # Send a GET request to the URL and get the response
#     soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content using BeautifulSoup

#     # Find all job listings based on the specific criteria (class = 'listing')
#     job_listings = soup.find_all('div', {'class': 'listing'})

#     for job in job_listings:
#         job_title = job.find('h6').find('a').text  # Extract the job title from the HTML structure
#         location = job.find('span').text  # Extract the location from the HTML structure

#         if 'Ajax' in location:  # Check if the location contains the desired location (Ajax)
#             email_subject = 'YO! You got some hiring in your desired location! GO CHECK IT OUT!!'  # Set the email subject
#             email_message = f"Job Title: {job_title}\nLocation: {location}"  # Set the email message
#             send_email(email_subject, email_message)  # Send the email
#             break  # Exit the loop after finding the first job

# class MyService(win32serviceutil.ServiceFramework):
#     _svc_name_ = 'MyPythonService'
#     _svc_display_name_ = 'My Python Service'

#     def __init__(self, args):
#         win32serviceutil.ServiceFramework.__init__(self, args)
#         self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
#         socket.setdefaulttimeout(60)
#         self.is_running = True

#     def SvcStop(self):
#         self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
#         win32event.SetEvent(self.hWaitStop)
#         self.is_running = False

#     def SvcDoRun(self):
#         servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
#                               servicemanager.PYS_SERVICE_STARTED,
#                               (self._svc_name_, ''))
#         schedule_job()

# def schedule_job():
#     # Schedule the job to run every day from Friday to Monday
#     schedule.every().friday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Fridays
#     schedule.every().saturday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Saturdays
#     schedule.every().sunday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Sundays
#     schedule.every().monday.do(scrape_amazon_jobs)  # Run scrape_amazon_jobs() on Mondays

#     # Keep the script running indefinitely
#     while True:
#         schedule.run_pending()  # Check if there are any scheduled jobs to run
#         time.sleep(30)  # Pause the script for 30 seconds

# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         servicemanager.Initialize()
#         servicemanager.PrepareToHostSingle(MyService)
#         servicemanager.StartServiceCtrlDispatcher()
#     else:
#         win32serviceutil.HandleCommandLine(MyService)


