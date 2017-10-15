#!/usr/bin/python


#--- IMPORT LIB AND MODULES ---#
#------------------------------#
try:
   import hashlib,optparse
   from time import sleep
   from os import system
except:
	print("\033[91m[!]\033[32m:Some Modules is Missing In Your\033[m [\033[96mPYTHON\033[m].\n\033[96m[*]\033[91m:\033[32mPlease Update Your Python or redownload ")
	exit()
#------------------------------#

#------------------------------------------ From Core Tool Folder -----------------------------------------#
													   #
try:													   #
   from Core.banner import banner,colors,cor								   #
   from Core.examples import examples									   #
except:													   #
	print(cor[3]+"\n[!]:"+cor[5]+"The ["+cor[4]+" Core"+cor[5]+" ]"+cor[3]+"Tool Folder Is Missing!!") #
	exit()												   #
############################################################################################################

#----------------------== VERSION ==-----------------------#
							   #
ver = cor[5]+"\nTool Version: [ "+cor[4]+"1.0"+cor[5]+" ]" #
							   #
#----------------------------------------------------------#


##################################### ERROR IN INPUT HASH #####################################
											      #
def errorhash():									      #
     print(cor[4]+"\n[x]:ERROR"+cor[2]+":"+cor[3]+"Please Enter Any Hash From This Hashes:")  #
     print(cor[2]+"""1 - MD5
2 - SHA1
3 - SHA224
4 - SHA256
5 - SHA384
6 - SHA512 """)										      #
											      #
###############################################################################################

#----------------------------------- DefaultBanner -----------------------------------#

defaultBanner = colors + """______  _____________________  __________      ________
___  / / /__    |_  ___/__  / / /_  ____/_____ ___  __/
__  /_/ /__  /| |____ \__  /_/ /_  /    _  __ `/_  /   
_  __  / _  ___ |___/ /_  __  / / /___  / /_/ /_  /    
/_/ /_/  /_/  |_/____/ /_/ /_/  \____/  \__,_/ /_/     
                                                 V[1.0]
"""
#-------------------------------------------------------------------------------------#

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ MAKE OPTIONS TOOL @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

parse = optparse.OptionParser(defaultBanner +cor[5]+ """Usage: python ./HASHcat.py [Options]

OPTIONS:
       -H <Multi Hash> -W <Wordlist>     ::> This Option For Brute Force Attack On This HASHES [ MD5,SHA1,SHA224,SHA256,SHA384,SHA512 ]

       -O --output <File Name>           ::> Use This Option If You Like Save The Resulit IN Output File.

+-------------+
|-v --version |::> SHOW TOOL VERSION.
|-e --examples|::> SHOW TOOL EXAMPLES.
+-------------+""",version=ver)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def main():
	parse.add_option("-H","--HASH",dest="hash",type="string",
								help="\nHASH please !\n")
	parse.add_option("-W","--wordlist",dest="wordlist",type="string",
								help="\nWordlist File Please!\n")
	parse.add_option("-O","--output",dest="outfile",type="string",
								help="\nFile Name Please !\n")
	parse.add_option("-v",action="store_true",dest="ShowVERSION",default=False,
								help="\nSHOW TOOL VERSION AND EXIT :)\n")
	parse.add_option("-e","--examples",action="store_true",dest="ShowEXAMPLES",default=False,
								help="\nSHOW TOOL EXAMPLES\n")

	(options,args) = parse.parse_args()

#=-=-=-=-=-=-=-=-=-=-=-=-=- START =-=-=-=-=-=-=-=-=-=-=-=-=-:)

	if options.ShowVERSION:
		print(ver)
		exit()

	elif options.ShowEXAMPLES:
		examples()
		exit()

	def checkoutfile():
	  try:
	     if options.outfile !=None:
			       return True
	  except:
		pass
	  return False

	check = checkoutfile()

	if options.hash !=None and options.wordlist !=None:
		hash = options.hash
		wl = options.wordlist
		try:
		   file = open(wl, "r")
		except:
		      print(cor[3]+"\n[!]:The [> "+cor[1]+wl+cor[3]+" <] File Not Found!")
		      exit()
		file = open(wl, "r")
		file2 = file.readlines()
		if len(hash) == 32: #MD5
			name = "MD5"
		elif len(hash) == 40: #SHA1
			name= "SHA1"
		elif len(hash) == 56: #SHA224
			name= "SHA224"
		elif len(hash) == 64: #SHA256
			name= "SHA256"
		elif len(hash) == 96: #SHA384
			name= "SHA384"
		elif len(hash) == 128: #SHA512
			name= "SHA512"
		else:
		     errorhash()
		     exit()

		loop = 1
		lens = len(file2)
		try:
                   system("clear || cls")
                   banner()
		   print(colors + "\n[+>]<====================> CONFIG <====================>[<+]\n"+cor[5])
		   print("[*]:HASH NAME    : "+colors+name+cor[5])
		   print("[+]:HASH         : "+hash[:30]+".....")
		   print("[+]:Wordlist     : "+wl)
		   print("[+]:Words Loaded : "+str(lens))
		   sleep(1.2)
		   print(cor[2]+"\n[*]:"+cor[1]+"Trying["+cor[4]+str(lens)+cor[1]+"] Password From Wordlist File....")
		   sleep(3.5)
		   for passwd in file2:

			   if len(hash) == 32: #MD5
			      hashcat = hashlib.md5(passwd.strip()).hexdigest()
			   elif len(hash) == 40: #SHA1
		              hashcat = hashlib.sha1(passwd.strip()).hexdigest()
		           elif len(hash) == 56: #SHA224
		              hashcat = hashlib.sha224(passwd.strip()).hexdigest()
		           elif len(hash) == 64: #SHA256
		              hashcat = hashlib.sha256(passwd.strip()).hexdigest()
		           elif len(hash) == 96: #SHA384
		              hashcat = hashlib.sha384(passwd.strip()).hexdigest()
		           elif len(hash) == 128: #SHA512
		              hashcat = hashlib.sha512(passwd.strip()).hexdigest()
		           else:
				errorhash()
				break
# START BRUTE-FORCE ATTACK:...
			   if hash == hashcat:
				if check == True:
					 outfile = options.outfile
					 file = open(outfile, "w")
					 file.write("\n[+]:HASH CRACK!:\n[*]:INFO:\n----------\n[*]:HASH Name:[ "+name+" ]\n[+]:HASH:[ "+hash+" ]\n\n[#>]:HASH CAT:[ "+passwd.strip()+" ]\n")
					 print(cor[1]+"\n[+]"+cor[4]+":"+cor[2]+"HASH CRACKER: AND The INFO Save In [ "+cor[4]+outfile+cor[2]+" ] output file :)")
					 break
				else:
					print(cor[1]+"\n[+]"+cor[4]+":"+cor[2]+"HASH CRACK!:\n"+cor[1]+"[*]"+cor[4]+":"+cor[2]+"INFO:"+cor[5]+"\n----------"+cor[1]+"\n[*]"+cor[4]+":"+cor[2]+"HASH Name:[ "+cor[4]+name+cor[2]+" ] "+cor[1]+"\n[+]"+cor[4]+":"+cor[2]+"HASH:[ "+cor[4]+hash+cor[2]+" ]"+cor[1]+"\n\n[#>]"+cor[4]+":"+cor[2]+"HASH CAT:[ "+cor[4]+passwd.strip()+cor[2]+" ]\n")
					break
			   else:
			       print(cor[3]+"\n[!]:Trying Password"+cor[5]+"["+cor[4]+str(loop)+cor[5]+"]  : "+cor[0]+str(passwd))
			       loop +=1
		   else:
			print(cor[4]+"\n[-]:"+cor[3]+"I WAS TRY ["+cor[4]+str(lens)+cor[3]+"] "+cor[3]+"Passowrd From [ "+cor[4]+wl+cor[3]+" ] Wordlist")
			print(cor[4]+"[x!]"+cor[3]+":PASSWORD NOT FOUND IN:[ "+cor[4]+wl+cor[3]+" ] Wordlist\n"+cor[2]+"[*]"+cor[4]+":"+cor[3]+"Try Other Wordlist :) ")
			exit()

		except KeyboardInterrupt:
			       print(cor[3]+"\n[!]:"+cor[4]+"Stoping Attack.....")
			       sleep(2)
			       print("Bye :)")
			       exit()

        else:
		print(parse.usage)
		exit()

if __name__=='__main__':
	main()

##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye

