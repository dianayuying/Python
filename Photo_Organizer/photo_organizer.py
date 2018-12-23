import shutil
import os
import glob
import time
import EXIF

source = 'C:\Photo\Ying_iPhone6S'
dest1 = 'C:\Photo\Ying_iPhone6S'


files = os.listdir(source)

for f in files:
    if (f.endswith(".JPG") ):
    #or f.endswith(".MOV")):
    
        with open(source+"\\"+f,'rb') as fh:
            tags = EXIF.process_file(fh, stop_tag='EXIF DateTimeOriginal')
            try:
                dateTaken = tags["EXIF DateTimeOriginal"]
                fldr = str(dateTaken)[:4]+"-"+str(dateTaken)[5:7]
                dest = dest1+"\\"+fldr
                if not os.path.exists(dest):
                    os.makedirs(dest)
                print(fldr)
            except:
                print("#####  No dateTaken...."+f)
                dest = ""
            #print(dateTaken)
            #print(type(str(dateTaken)))
        
        if (len(dest)>0):
            # if shutil.move() destination is a full path including filename, then it is overwrite
            shutil.move(source+"\\"+f, dest+"\\"+f)
    elif (f.endswith(".MOV")):
    
# File Date/Time is not the photo action Date/time.  Use EXIF to get the information
        dest = dest1+"\\"+time.strftime('%Y-%m',time.gmtime(os.path.getmtime(source+"\\"+f)))
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.move(source+"\\"+f, dest+"\\"+f)
        #print(dest)
