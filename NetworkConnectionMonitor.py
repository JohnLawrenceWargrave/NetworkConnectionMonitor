import os
import re
import subprocess
import time

def speedtest ():    
    response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

    ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
    download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
    upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

    try:
        ping = ping[0].replace(',', '.')
        download = download[0].replace(',', '.')
        upload = upload[0].replace(',', '.')
    
    except:
        pass

    try:
        f = open('/home/pi/yourFolder/yourFile.csv', 'a+')                      #opens or creates your file 
        if os.stat('/home/pi/yourFolder/yourFile.csv').st_size == 0:            #if there was no file it writes the first line in the File
            f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
    except:
        pass


    f.write('{},{},{},{},{}\r\n'.format(time.strftime('%d/%m/%y'), time.strftime('%H:%M:%S'), ping, download, upload)) #seconds are just necessary to adjust the timer, since the test needs about 30s it has no significance for the data
    f.close()
    
while 1:
    speedtest()
    time.sleep(270)
