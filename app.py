import streamlit as st
from functions.gmail import send_email
from functions.db_functions import get_roles

# Title
st.title("Bulk Emailer ✉️")

st.subheader("Enter Credentials ")
email_id  = st.text_input("Enter email:")
app_pass = st.text_input("Enter app password:")

role = st.multiselect(
    'What are your favorite colors:',
    ['Professor', 'Staff'])

st.write('you selected:', role)

# load all recipients 
roles_df  = get_roles(role)
st.write("{} emails selected".format(len(roles_df)))
subject = st.text_input('Email subject:')
body = st.text_area('Email body:')

# iterate over all recipients, form email body and send mail

if st.button("Send ->"):
    total_iterations = len(roles_df)

    # Create a progress bar
    progress_bar = st.progress(0,text="Sending Emails...")

    # Iterate over each row in the DataFrame
    for i, row in enumerate(roles_df.to_dict(orient="records")):
        # Update the progress bar
        progress_bar.progress((i + 1) / total_iterations)

        # Create prefix
        if row["role"] == "Professor":
            prefix = "Dear Professor {0},\n\n\n".format(row["last_name"]) 
        elif row["role"] == "Staff":
            prefix = "Dear {0},\n\n\n".format(row["first_name"])    
            
        # Set up the message parameters
        to = row["email_id"]
        file_attachment = "attachment/Resume-da.pdf"
        footer = "\n\n\nRegards,\nParva Shah"
        mail_text = prefix + body + footer
        
        # Send the email
        send_email(email_id, app_pass, to, subject, mail_text, file_attachment)

    st.write("{0} emails sent!".format(len(roles_df)))

    
