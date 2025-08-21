Description: This script will take the input of a find command looking for root owned binaries with the SUID set and then parse the file to see if the GTFO bins has a SUID entry, if not it will tell me what other entries it did have.

Instructions: 
Download and save the script

Install dependencies:
pip install requests beautifulsoup4
note: this is already on kali natively so you can skip this step if you're on an updated kali box


Generate your input file on the target machine (example for finding root owned binaries with SUID):

find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null > binaries.txt

Copy / paste the output of that command to a file on your attacking machine


Run the script:

python3 check-binaries.py suid_list.txt


Output example:

python3 check_suid.py test.txt
[*] Checking 14 binaries against GTFOBins...

[ ] chfn -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/chfn/)
[ ] chsh -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/chsh/)
[ ] dbus-daemon-launch-helper -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/dbus-daemon-launch-helper/)
[ ] dmcrypt-get-device -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/dmcrypt-get-device/)
[+] find -> SUID FOUND (https://gtfobins.github.io/gtfobins/find/)
[ ] fusermount -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/fusermount/)
[ ] gpasswd -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/gpasswd/)
[-] mount -> No SUID entry, found: Sudo (https://gtfobins.github.io/gtfobins/mount/)
[ ] newgrp -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/newgrp/)
[ ] passwd -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/passwd/)
[ ] ssh-keysign -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/ssh-keysign/)
[-] su -> No SUID entry, found: Sudo (https://gtfobins.github.io/gtfobins/su/)
[-] sudo -> No SUID entry, found: Sudo (https://gtfobins.github.io/gtfobins/sudo/)
[ ] umount -> Not found on GTFOBins (https://gtfobins.github.io/gtfobins/umount/)
