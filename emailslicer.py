def my_email_slicer(email=input('Please advise your email address: ')):
    user=email[:email.index("@")]
    domain=email[email.index("@")+1:]
    print("Your email is {}, user {}, domain {}.".format(email,user,domain))

my_email_slicer()