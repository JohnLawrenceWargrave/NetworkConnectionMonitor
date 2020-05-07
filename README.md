# NetworkConnectionMonitor
A simple Python tool, to track your network Connection and store it in a csv file.
 
I used mainly the code of this side: https://pimylifeup.com/raspberry-pi-internet-speed-monitor/
and added a loop with a timer and some try cases to catch the errors which appear when you have no connection.

You need to have python 3 installed, also the Python Package Index and the speedtest client which is in the pip repository
sudo apt-get install python3-pip
sudo pip3 install speedtest-cli

You can test if this works by typing: speedtest-cli

