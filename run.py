from PyMessenger import Email, SMS, Messenger
import ScrapeRates as sr
import schedule
import time

#send daily mortgage rates to participating phone numbers every day at 4:05PM 
def job():
    
    currentRates = sr.ScrapeRates()
    rates = "".join(currentRates)
    my_messenger = Messenger('antoniofs23', 'ybxl vhbl qwoy lxid') #username / pass

    # all of the enlisted phone numbers
    num2send = ['7862711159']

    for num in num2send:
        # Build the message
        number    = num # Example US phone number
        gateway   = '@tmomail.net' # For a tmobile number
        subject   = 'Automated: CurrentMortgageRates 30-year Fixed:'
        body      = rates
        msg       = SMS(number, gateway, subject, body)

        # Send the message
        my_messenger.send_sms(msg, one_time=True)
    
    return

schedule.every().day.at("16:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

# to kill all running processes in the terminal
# ps -ef >> view running processes
# kill -9 ID [3rd col is ID] >> for kill process

## ps aux | grep java
## killall python