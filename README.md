# Automatic Birthday Wishes via Email

## Description
Are you tired of manually sending birthday wishes to your friends? This Python script allows you to automatically send birthday wishes via email to your friends on their special day. Simply update a CSV file with your friends' birthdays, set up your email details, and let the script do the rest!

## Setup
1. Update the following variables in the script with your information:
   - `MY_EMAIL`: Your email address.
   - `MY_PASSWORD`: Your email password or app password if required.
   - `SMTP_ADDRESS`: Your SMTP server address for sending emails. You might need to check your email provider's documentation for the correct SMTP settings.
   - Ensure your email provider allows less secure apps or generate an app password if required.

2. Update the `birthdays.csv` file to contain today's month and day for the birthdays you want to celebrate.

## Automation
To automate the birthday wishes, follow these steps:

1. Create an account on PythonAnywhere cloud service, which is free to register.

2. Upload your Python script to PythonAnywhere.

3. Set up a scheduled task on PythonAnywhere to run your script daily or at a specific time to check for birthdays and send wishes accordingly.

## Note
Ensure you handle your friends' data responsibly and in compliance with privacy regulations.

## Disclaimer
Sending automated emails may require consent from the recipients and adherence to email regulations to avoid being marked as spam. Use this script responsibly and with consideration for others' preferences.

## Credits
This project was inspired by the need for a simple and automated way to send birthday wishes. Developed by me.
