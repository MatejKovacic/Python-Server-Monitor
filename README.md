Simple Python Server Monitor
============================

Super simple Python based server ping monitor. Emails you with any email address (default: Gmail) if server is down.

Adding Sites
------------

You can add multiple sites to check every minute with the monitor.

1. Open up the configuration.py file

2. Add your site's to the list there. For example, the configuration for checking google and github would be:

        sites = [
            ('Google', 'www.google.com', ['recipient1@acme.com', 'recipient2@acme.com']),
            ('Yahoo', 'www.yahoo.com', ['recipient3@acme.com'])
        ]

    **Note:** Python syntax for arrays and tuples must be obeyed (watch for commas)!


Configuration for Gmail (Easiest)
---------------------------------

Open the configuration.py file with your favorite text editor.

1. Add the Gmail address you would like to send the email from when your server goes down.

        "monitor_email": 'your_gmail_username@gmail.com',

2. Add the Gmail password that is associated with the above Gmail email address

        "monitor_password": 'gmail password',

3. Add script to crontab to run every x amount of minutes you would like to run it.


Configuration for a custom email account
----------------------------------------

Open the configuration.py file with your favorite text editor.

1. Add the email address you would like to send the email from when your server goes down.

        "monitor_email": 'your_gmail_username@yourdomain.com',

2. Add the email password that is associated with the above email address

        "monitor_password": 'email password',

3. Set the email server (smtp) address to send the emails from

        "email_server": 'smtp.yourdomain.com',

4. Set the email server port

        "email_server_port": 587,

5. Add script to crontab to run every x amount of minutes you would like to run it.


Optional Settings
-----------------

You can optionally set the subject of the email that is sent when the server goes down

    "email_subject": 'Subject of the email'

