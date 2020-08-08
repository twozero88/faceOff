from cha0s import text
import os
import shutil
text()
print('-----Setup for faceOff-----')
ch1 = int(input('How many seconds to trigger the screen off when someone is not present ? : '))
ch2 = input('Do you want to autostart the script on startup ? y/n : ')
ch3 = input('Do you want to show the face captures continuously ? y/n : ')
print('Not running the script in background in case you need to close it while watching a movie at night ;-)')
with open('config','w') as f:
	f.write(str(ch1)+'\n')
	f.write(str(ch2)+'\n')
	f.write(str(ch3))
if ch2=='y' and not os.path.exists('C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\fO - Shortcut.lnk'):
	user = os.environ['USERPROFILE'].split("\\")[-1]
	src = os.getcwd()+"\\fO - Shortcut.lnk"
	dest = "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\fO - Shortcut.lnk"
	shutil.copyfile(src,dest)
input('Setup Commplete.')