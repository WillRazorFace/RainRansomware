# RainRansomware
![alt text](https://imgur.com/sxy6xMv)
Interested in the word ransomware in the repository? Do you like cryptography? Or just want to fuck some people's computer? Right. I'm developing this ransomware, and its name is Rain (kek), after all, when any ransomware starts its standard process is like acid rain. I am using 32-byte AES encryption and I want to add other related features as I learn how other forms of encryption work. Its first version is being written in Python and later I intend to pass it to C ++ as well. You can also help me if you want, I need to compile the code in py so that I have an exe file, and at the moment I do not know how to do this with so many libraries contained in the project. Everything will be appreciated, from testing the malware to adding the most useful features. Rain Ransomware works like this:

- Firstly it imports some libraries to facilitate the run in directories and other manipulations of the OS (glob, the, pycrypto, platform, etc)
- Checks if the OS of the infected machine is Linux or Windows, executing two different structures for each one
- After the scan creates some malicious files useful for malware persistence, deactivating native antivirus and UAC, besides adding a registry in the machine (Windows only, for now)
- Encrypts files with certain extensions (new extensions are welcome) in three main directories, which usually save the most important files (Desktop, Documents and Downloads)
- Swap Desktop Background for malware logo
- It continues encrypting the entire partition in question

Suggestions for improvements? Please leave them there. Let's make this something more than an ambitious teen project.
Contact me:
retroniet@outlook.com
retr0c0de@outlook.com
