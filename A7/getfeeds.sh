rm newfeeds.txt
touch newfeeds.txt
#Get feeds uses curl command from slide notes and extracts xml file from blog list

file="output.txt"
while IFS= read -r line
do
line=${line%$'\r'}

    curl "${line}" | grep -n "rss+xml" |  grep -Eo 'http://[^ >]+' | head -n 1 | cat >> newfeeds.txt

done <"$file"


