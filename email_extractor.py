#Extracting domain name and user name from emails

email = input('Enter your email address').strip()

userName = email[:email.index('@')]
domainName = email[email.index('@')+1:]

print(f'Your username is {userName} and domain name is {domainName}')
