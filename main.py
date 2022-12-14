import smtplib
from email.message import EmailMessage
import datetime as dt
import pandas as pd
import cred


my_email = cred.my_email
my_email_password = cred.my_email_password



def send_email(receiver) :
    rec_email = new_dict[receiver][1]
    
    msg = EmailMessage()
    msg["subject"] = "Happy Birthday"
    msg["title"] = f""
    wish = f"""Hey {receiver}\n, 
    Happy birthday. All the best for the upcoming year.May you reach new heights 🤍🤍
    \n
                with love murali!!"""
    msg.set_content(wish)
    with smtplib.SMTP("smtp.gmail.com",587) as connection :
        connection.starttls()
        connection.login(user=my_email, password=my_email_password)
        print(f"sending mail to {receiver}")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=rec_email,
            msg=msg.as_string() )
        print("email sent")

now = dt.datetime.now()
today_date = now.day
today_month= now.month
today = (today_date, today_month)

sheet_id = "1eZiYBHrWEu5FLThZMsEy5CGZepMvg5k8Tok1Nc4LpNA"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
bday_df = pd.read_csv(url, index_col=0)

bday_dict = bday_df.to_dict(orient="index")
new_dict = {key :[list(map(int,value["dob"].split("/"))), value["mail_id"]] for (key, value) in bday_dict.items()}

for smt in new_dict:
    bday =  tuple(new_dict[smt][0][0:2])
    if today == bday :
        send_email(smt)
