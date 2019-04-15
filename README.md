# RainRansomware
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

Changes:
  - Complete restructure/rebuild using oop
  - Removed "partition" encryption functionality as it would take too long and the important files such as documents, desktop, etc are already encrypted
  - The password used to derive the AES key is dumped to disk once encryption is complete this is obviously in secure but allows for decryption. A better approach would be the encrypt the password with an RSA public key before dumping and keep a private copy of the private key. Then when you want to decrypt the files just decrypt the AES password and feed it into the RainDecrypter class.
  - Added an encryption class which uses secure key div and encrypts in blocks
  - Added a much quicker file iteration/directory walking class
  - Comments and Docs (where relevant)
   
TODO's/Considerations:
 - It is possible to specify resource files with pyinstaller instead on embedding them into the source, look at the `__set_back_ground_windows` method to gauge a better understanding.
 - I haven't got round to testing the scripts so I’m not sure how well it will work but the added classes have been toughly tested and work as intended.
 - When I get a chance, I'll build a exe using pyinstaller
 - Two functions in the RainDecrypt are incomplete I’ll leave them to you
 - Use a IDE something like PyCharm it helps to keep your code tidy and types consistent
 
I was kinda board so decide to commit to your project. Any issues or features you want to add let me know.

   
   
