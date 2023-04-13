# Bulk Emailer 📬
This is a simple bulk emailer application that allows you to send emails to multiple recipients at once. You can upload a CSV file as a database containing the list of recipients, filter them based on college and role, and customize the email subject, prefix, and body. You can also attach a PDF file as an attachment to the emails.

## How to Use
1. Enter your email address and app password: Start by entering your email address and app password in the respective text input fields. If you don't have an app password, you can follow this [link]("https://support.google.com/mail/answer/185833?hl=en") to learn how to generate one.

2. Upload Database (CSV): Click on the "Choose File" button to upload a CSV file containing the list of recipients. The CSV file should have columns for 'college', 'role', 'first_name', 'last_name', and 'email_id'.

3. Select College and Role: Once the database file is uploaded, you can select the college and role of the recipients you want to send the email to using the respective dropdown menus.

4. View Filtered Recipients: The filtered recipients based on college and role will be displayed below the dropdown menus. You can see the number of recipients and their details in the table.

5. Enter Email Details: Enter the email subject, prefix, and body in the respective text input fields. You can use tags in the prefix which will be replaced by the corresponding column values when sending the email. For example, you can use "<first_name>" and "<last_name>" tags in the prefix, and they will be replaced with the actual first name and last name of the recipient.

6. Upload Attachment: If you want to attach a PDF file to the emails, you can click on the "Choose File" button and upload the file.

7. Send Emails: Click on the "Send ->" button to start sending the emails. The progress bar will show the progress of the email sending process. The application will automatically sleep for 10 seconds after sending every 10 emails to avoid reaching the rate limit of the email provider.

8. Email Sent: Once all the emails are sent, you will see a message showing the number of emails sent.

Note: Please make sure to double-check all the email details and recipients before sending the emails to avoid any mistakes. Also, be mindful of the email provider's terms of service and rate limits to avoid any issues with your email account.

That's it! You can use this bulk emailer application to send emails to multiple recipients quickly and easily. Happy emailing! 📧😊

## Demo

![](https://github.com/parvashah-create/personalized-bulk-mailer/blob/main/bulk-mailer.gif)
