import requests
from datetime import datetime
import smtplib


def is_night():
    para = {
        'lat': 19.033049,
        'lng': 73.029663
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=para)
    data = response.json()['results']
    sunrise = data['sunrise'].split(":")[0]
    sunset = data['sunset'].split(":")[0]
    now = datetime.now().time().hour
    if int(sunrise) > int(now) < int(sunset):
        return True


def iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()['iss_position']
    longitude = float(data['longitude'])
    latitude = float(data['latitude'])
    my_latitude = 19.033049
    my_longitude = 73.029663
    if my_latitude - 5 <= latitude <= my_latitude + 5 and my_longitude - 5 <= longitude <= my_longitude + 5:
        return True


my_mail = 'YOURMAIL@gmail.com'
my_password = 'YOURPASSWORD'
if is_night():
    if iss_location():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=my_mail, password=my_password)
        connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg='SUBJECT:HEY ISS IS ON YOUR HEAD\n\n'
                                                                     'hey YOURNAME look there is worlds most'
                                                                     ' expensive thing on your head now '
                                                                     'you are richer than the queen')
        connection.close()
        print("mail sent")
else:
    print("not sent")