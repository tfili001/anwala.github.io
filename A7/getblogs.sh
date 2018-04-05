rm blognames.txt
touch blognames.txt
clear
n=30


line (){ 
    printf "_______________________________________________________________________________\n"
		
}

 for i in `seq 1 $n`;
        do clear
                 
            	printf "Loading URLs "$i/$n"\n"
                line
                curl -I -L 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117' | grep -Eo '(http|https)://[^/"]+' | awk {'print $1'} | tr -d ';' | sort -u | cat >> blognames.txt

        done   

cat blognames.txt
