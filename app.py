import streamlit as st
from functions.gmail import send_email
import pandas as pd
import time

# Title
st.title("Bulk Emailer 📬")
email_id  = st.text_input("Enter email:")
app_pass = st.text_input("Enter app password:")
st.write("Here is how you can get your app password: [link](https://support.google.com/mail/answer/185833?hl=en)")

# Upload database file
db_file = st.file_uploader("Upload Database (CSV)", type=["csv"])
if db_file is not None:
    df = pd.read_csv(db_file)

    college = st.selectbox("Select college",df.college.unique())
    role = st.multiselect(
        'Select role:',df.role.unique())

    # Filter and display recipients
    roles_filter_df  = df[df['role'].isin(role)]
    college_filter_df = roles_filter_df[roles_filter_df['college']==college]
    st.write("emails selected: {}".format(len(college_filter_df)))
    st.write(college_filter_df)

    # Email details
    subject = st.text_input('Email subject:')
    st.write("""
    prefix is how you want to start your mails. You can use tags which will replaced by column value when sending the mail\n
    Example: Dear Professor <first_name> <last_name>\n
    Output: Dear Professor Parva J Shah 
    """)

    prefix_template = st.text_input(f"Enter prefix for the mails")

    body = st.text_area('Email body:')

    # Upload attachment file
    attachment_file = st.file_uploader("Upload Attachment", type=["pdf"])

    # Iterate over all recipients, form email body, and send mail
    if st.button("Send ->"):
        total_iterations = len(college_filter_df)

        # Create a progress bar
        progress_bar = st.progress(0,text="Sending Emails...")

        # Iterate over each row in the DataFrame
        for i, row in enumerate(college_filter_df.iloc[:].to_dict(orient="records")):
           

            # Create prefix
            replace_first_name = prefix_template.replace("<first_name>",row["first_name"])
            replace_last_name = replace_first_name.replace("<last_name>",row["last_name"])
            prefix = replace_last_name + "\n\n\n"

            # Set up the message parameters
            to = row["email_id"]
            file_attachment = attachment_file if attachment_file is not None else None

            mail_text = prefix + body
            # Sleep for 10s for every 10 emails sent
            if i % 10 == 0:
                time.sleep(10)

            # Send the email
            send_email(email_id, app_pass, to, subject, mail_text, file_attachment)
             # Update the progress bar
            progress_bar.progress((i + 1) / total_iterations)

            st.write(to, "email sent!")
        st.write("{0} emails sent!".format(len(college_filter_df)))
