rm blognames.txt
touch blognames.txt

 for i in `seq 1 98`;
        do
                 
            	ewprintf $i"______________________________________\n"
		curl -I -L 'http://www.blogger.com/next-blog?  navBar=true&blogID=3471633091411211117' | grep -Eo '(http|https)://[^/"]+' | awk {'print $1'} | tr -d ';' | sort -u | cat >> blognames.txt

        done   


