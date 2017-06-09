. ~/.keychain/raspberrypi-sh
cd /mnt/freebox/darkness/
ssh root@51.15.76.14 /root/normalize.py
files=$(ssh root@51.15.76.14 ls /home/rtorrent/sync/)
#for all the files on remote folder, start a sync
for p in $files
do 
    #check if file exist localy
	echo $p
    if test -f 51.15.76.14/$p
    then    
		 echo 'sync in progress'
    else 
		echo 'wget -r --no-passive --no-parent  ftp://lapinrose33:Pacific888@51.15.76.14/'$p
        echo 'ssh root@51.15.76.14 rm /home/rtorrent/sync/'$p
		touch 51.15.76.14/downloading$p
        wget -r --no-passive --no-parent  ftp://lapinrose33:Pacific888@51.15.76.14/$p
		rm 51.15.76.14/downloading$p
	    ssh root@51.15.76.14 rm /home/rtorrent/sync/$p
    fi
done