# Text Message Server
This small python server creates an endpoint at `yourserver.com:8088/index`

This server was put in use during a [lockdown](http://krqe.com/2015/12/11/albuquerque-police-city-hall-on-lock-down/) at the City of Albuquerque. The front end queried a database of phone numbers for Municipal Development and sent the supplied message to everyone.  

### Parameters

| Param | Value |
|-------|-------|
|  to|For text message: the phone number @ sms gateway. Verizon gateway is vtext.com. For email, just use the email address x@y.com|
|theMSG | text to send|


### Sample Usage
`yourserver:8088/index?to=5051234567@vtext.com&theMSG=This is a test of the Dept MSG System`

From a webpage, simply use `window.open(URL)`. The application will redirect to a confirmation stating `Mail sent to: xxx@y.com`

The application accepts a comma separated list of email addresses/phone numbers to send to multiple recipients. 
