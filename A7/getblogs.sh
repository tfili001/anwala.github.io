rm input.txt
touch input.txt
rm output.txt
touch output.txt
clear

n=200

line (){ 
    printf "_______________________________________________________________________________\n"		
}
url="http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"

 for i in `seq 1 $n`;
        do clear
                 
            	printf "Getting Blog URLs "$i/$n"\n"
                line
                curl -I -L $url  | grep -E '^Location:' | awk '{print $2}' |  cat >> input.txt
        done   

# Remove duplicates
sort input.txt | uniq > output.txt
sed -i 'blogger/d' output.txt
clear

printf "Gathering Complete "$n/$n"\n"

cat output.txt
