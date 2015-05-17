import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import re, uuid
# Change to your own account information
to_addr = 'dels@dels.info; martin.delisle@oracle.com'
gmail_user = 'smtp.generic.dels@gmail.com'
gmail_password = 'taleo123'
today = datetime.date.today()
hostname = socket.gethostname()
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
mac_addr = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
my_ip = '%s\'s ip is %s and the mac is: %s' %  (hostname, ipaddr, mac_addr)
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For %s on %s' % (hostname, today.strftime('%b %d %Y'))
msg['From'] = gmail_user
msg['To'] = to_addr
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
smtpserver.sendmail(gmail_user, [to_addr], msg.as_string())
smtpserver.quit()
