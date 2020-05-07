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
        f = open('/home/pi/ownCloud/NetworkMonitoring/speedtest.csv', 'a+')
        if os.stat('/home/pi/ownCloud/NetworkMonitoring/speedtest.csv').st_size == 0:
            f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
    except:
        pass

    try:
        f.write('{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), ping, download, upload))
        f.close()
        
    except:
        f.write('{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), 'no connection', 0, 0))
        f.close
    
while 1:
    speedtest()
    time.sleep(270)