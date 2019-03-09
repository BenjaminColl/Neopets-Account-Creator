# Neopets-Account-Creator
This will create accounts for you on neopets.com

Requirements:
- Python 3.7
- requests

Auto Activation:

- For now, this only supports gmail accounts
- Login to your gmail accounts in a web browser then do the following:
- Go to your Google Account.
- On the left navigation panel, click Security.
- On the bottom of the page, in the Less secure app access panel, click Turn on access.
- After doing this, open Account Creator.py, locate the function "def Activation(self):" After you find this function add in your username and password into the sections in this line "activation = ReadEmail.GetActivation('Username@gmail.com', 'Password')"
- After you do this, run the creator it will now create an account for you, then login to your email account, find an email with the subject of "Neopets - Welcome and Account Activation". Then it'll get the activation link, activate your account for you, delete the previous email and stop.

Usage:

1 - Open the Account Creatory.py file
<br>
2 - Enter the required information
<br>
3 - View your account details saved to Accounts/Output.txt
<br>
4 - Output gets saved in the following format: Username:Password:Email:Birthday

<img src="https://i.imgur.com/TdGdkxF.png" /></a>
<br>
<img src="https://i.imgur.com/Hyz0Bve.png"/></a>
