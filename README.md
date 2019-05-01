# RainRansomware
Interested in the word ransomware in the repository? Do you like cryptography? Or just want to fuck some people's computer? Right. I'm developing this ransomware, and its name is Rain (kek), after all, when any ransomware starts its standard process it's like acid rain. I am using 32-byte AES encryption and want to add other related features as I learn how other forms of encryption work. Everything will be appreciated, from testing the malware to adding the most useful features. Rain Ransomware works like this:

- First of all it imports some libraries to facilitate the execution in directories and other manipulations of the operating system (glob, os, pycrypto, platform, etc)
- Checks if the operating system of the infected machine is Linux or Windows, running two different structures for each one
- After the scan saves the key to be used in the encryption on a certain area of ​​the disk so that the decryption process can occur.
- There are functions only for Windows like changing the background of the Desktop and creating a key in the registry of the computer to increase the persistence (in previous commits the program also created two bat files to try to disable Windows Defender and UAC.I think there is no need, because in all the anti-virus I tested Ransomware goes unnoticed. If you want to include these functions I will be very grateful as well. On Linux I have not yet found a reasonable way to change the background and create persistence files that work in most distros. This is something that would greatly increase the functionality of the program.
- Encrypts files with certain extensions (new extensions are welcome) in three main directories, which usually save the most important files (Desktop, Documents and Downloads)
- Still encrypting the entire partition in question

The decryption script goes the other way and is easy to understand

- First of all it imports some libraries to facilitate the execution in directories and other manipulations of the operating system (glob, os, pycrypto, platform, etc)
- Checks if the operating system of the infected machine is Linux or Windows, running two different structures for each one
- After the scan, in the case of a Windows system, it returns the background of the computer to the original, deletes previously
generated malicious files, deletes the values entered in the registry of the computer and searches for the generated key to decrypt the files. On Linux, just look for the key.
- Decrypts files with the extension "rain" in three main directories, which usually save the most important files (Desktop, Documents and Downloads)
- Continue decrypting the entire partition in question

You can analyze all the main functions in the function file (Source-Code/Func.py). In future commits I want to add the time counting feature in that somehow, even the computer having been turned off at some point, counting will continue to increase when it is turned on. When 72 hours have elapsed, files with the extension "rain" will be deleted. In addition, I think it would be best to add a graphical interface to the program, containing information such as Bitcoin/Ethereum to be paid for the redemption, remaining time before files are deleted, and so on. I tried to do some shit on Tkinter but believe me, I'm much worse there. So if you can help me with any of these things (mainly with the GUI) a good part of that repository would be due to you.

Suggestions for improvements? Please leave them there. Let's make this something more than a high school teen project. Please contact me: guilherme.violin@hotmail.com. I have Skype too (I know no one else uses it, fuck it): spiderman20hacking@outlook.com
