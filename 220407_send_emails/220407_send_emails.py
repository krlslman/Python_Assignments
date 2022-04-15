# Allow less secure apps first : https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Mm9e0_M6ijQ14K5o5KnPjQ6D9CTUHqnt-wZaigWyKVGOyxYPIqsGtRPL5Ye7frM6zE3dnWBxENudHWLqCskPLFnWCWwQ 
import smtplib
password = "yourpasswordhere"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login("selmankorall", password)
message = "\n This mail is sent via vscode. Hope you are doing fine. \n Sincerely,\nKoral"
mails = ["selmankorall@gmail.com"]
server.sendmail("selmankorall@gmail.com", mails, message)
server.quit()
