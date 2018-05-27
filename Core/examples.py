try:
   from banner import banner,cor
except:
      print(cor[4]+"\n[!]:"+cor[3]+"Error: The [ "+cor[4]+"banner.py"+cor[3]+" ]Tool File Is Missing!!")
      exit(1)

def examples():
	banner()
	print(cor[5]+"""\n
EXAMPLES:

#[MD5]:
           ./HASHCat.py -H 5d41402abc4b2a76b9719d911017c592 -W /root/Desktop/wordlist.txt
#[SHA1]:
      	   ./HASHCat.py -H aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d -W /root/Desktop/wordlist.txt
#[SHA224]:
	   ./HASHCat.py -H ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193 -W /root/Desktop/wordlist.txt
#[SHA256]:
	   ./HASHCat.py -H 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 -W /root/Desktop/wordlist.txt
#[SHA384]:
	   ./HASHCat.py -H 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c1c5d-..... -W /root/Desktop/wordlist.txt
#[SHA512]: 
           ./HASHCat.py -H 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e.... -W /root/Desktop/wordlist.txt
------------------------------------------------------------------------------------------------------------------------------------------------

Note: Note: if you like save the crack info try [ -O ] and set file name to save info in the file

ex:
   ./HASHCat.py -H 5d41402abc4b2a76b9719d911017c592 -W /root/Desktop/wordlist.txt -O file.txt 


------------------------------------------------------------------------------------------------------------------------------------------------

To Create Some Hash

./HASHCat.py -H md5 -T Python

""")

