from PyMessenger import Email, SMS, Messenger
import ScrapeRates as sr
import schedule
import time

def job():
    
    currentRates = sr.ScrapeRates()
    rates = "".join(currentRates)
    my_messenger = Messenger('username', 'password') #username / pass

    # all of the enlisted phone numbers
    num2send = ['phone number']

    for num in num2send:
        # Build the message
        number    = num # Example US phone number
        gateway   = '@tmomail.net' # For a tmobile number
        subject   = 'subject'
        body      = 'body'
        msg       = SMS(number, gateway, subject, body)

        # Send the message
        my_messenger.send_sms(msg, one_time=True)
    
    return

#can run in the background as a nohub request
schedule.every().day.at("16:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
