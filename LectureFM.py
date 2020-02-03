#!/usr/bin/env python3
#LectureFM Project - Galaxia Kristu Jayanti College Fest
#Applied Ecectronics + Computing Python Project
#Designed and Developed with help or online codes with source attribution made to the 
#original creators and forums that helped with the project.
#Project Developed by Joel Celesia and Pooja Shree BP

#update Crontab: */5 9-16 * * 1-5 /home/Desktop/LectureFM/LectureFM.sh >/dev/null 2>&1
from os import system as sys
from time import sleep
from datetime import datetime
from ftplib import FTP
from os import chdir # this is to set the directory to LFM Dir



def ftpfun(filename):
    '''
		ftp function that takes in a string of filename 
		uploads the file to remote ftp server
		after which it will reset the file permissions to 755
		to allow the users to see it and download.
    '''
    domain = 'domainName.url'
    username='ftpusername'
    password='Pa$$w0rd'
    directory= '/destination/folder/name'
    
    try:
        #FTP Login
        ftp = FTP(domain) # creates an object to the 
        ftp.login(user=username,passwd=password)
        ftp.cwd(directory)

        file=open(f'/home/pi/Desktop/LectureFM/{filename}','rb')
        
        ftp.storbinary(f'STOR {filename}', file)
        file.close()                                    # close file and FTP
        ftp.sendcmd('SITE CHMOD 755 ' + filename)
        ftp.quit()
        return
    except Exception as e:
        print(f'{e}')
        return

def main():
	'''
		Main Function that initates the program.
		this function generates filename with the current
		date and time to create a uniquie name
		this function also uses the Rasberry Pi's internal
		ALSA Audo Drivers to connect system registed bluetooth
		device as input and record the audio via bluetooth
		using arecord function
	'''
    sec = str(10) 
    '''
    	Time set in number in seconds 60*3 is three minute we 
    	we can set the values to whatever time slot you want 
    	for you are only limited by the resources you provide
    	to the rasberry pi. the longer you run the hoter the 
    	Pi gets please remember that.
    '''

    n = datetime.now() # datetime object to generate an uniquie filename.

    try:
        filename = f'LFM_{n.strftime("%d.%m.%Y_%H.%M")}.mp3' # LFM_29.01.2020_10.15.mp3
        cmd = f'arecord -d {sec} -f U8 {filename}' # Command to record the audio
        chdir('/home/pi/Desktop/LectureFM') # set the current working directory
        
        sys(cmd)  
        sleep(10)
        ftpfun(filename)
    except Exception as e:
        print(f'there was an error: {e}') # ex. there was an error: arecord failed to record #12-3434 ALSA Driver

if __name__=='__main__':
    main()
