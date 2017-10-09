"""
Required Settings:

sites = array of triples:
    [('nicename', 'hostname/ip', array of recipient emails: ['email1', email2', ...]), ...]

    nicename          - Name used in Subject: instead of hostname/ip
    hostname/ip       - Hostname/IP address of the server to check
    recipient emails  - Emails where downtime alerts will be sent to

settings = dictionary:
    {'key': value, ...}

    monitor_email     - Email address to be sent from (sender)
    monitor_password  - Password of the email address to be sent from
    email_server      - Email server to send the emails from
    email_server_port - Email server smtp port

Optional Settings:

    email_subject     - The subject of the email to send

"""
sites = [
    ('Google', 'www.google.com', ['recipient1@acme.com', 'recipient2@acme.com']),
    ('Yahoo', 'www.yahoo.com', ['recipient3@acme.com'])
]

settings = {
    'monitor_email': 'sender@acme.com',
    'monitor_password': 'password',

    # Leave as it is to use gmail as the server
    'email_server': 'smtp.gmail.com',
    'email_server_port': 587,

    # Optional Settings
    #'email_subject': 'Server Monitor Alert'
}
