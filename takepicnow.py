#to start enumerate over, sudo rm /home/pi/Documents/pic_temp.txt
#** this will start overwriting any pics that exist in Desktop/Pictures dir.

from picamera import PiCamera
from time import sleep
import os
from subprocess import call
import sys
import datetime

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = "/home/pi/Documents/instantpic_temp.txt"
camera = PiCamera()
camera.rotation = 180

def setup2():
    with open(filename,"w") as writefile:
        writefile.write("0")
        writefile.close()
    setup()

def setup():
    if os.path.exists(filename) != 1:
        setup2()
    else:
        global picnum
        picnum = int(open(filename,"r").readlines()[0])    

def loop(picnum):
            uppath = current_dir + "/dropbox_uploader.sh upload "
#    while True:

            date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
            picnum += 1
            camera.annotate_text=str(date_time)
            picfile = '/home/pi/Desktop/Pictures/image%s.jpg' % picnum
            camera.capture(picfile)
            with open(filename,"w") as writefile:
                writefile.write(str(picnum))
                writefile.close()
            try:
                call([uppath + picfile + " image" + str(picnum) + ".jpg"],shell=True)
            except:
                print "upload failed"
                destroy()
            destroy()
def destroy():
    sys.exit()

if __name__ == '__main__':
    setup()
    try:
        loop(picnum)
    except KeyboardInterrupt:
        destroy()
