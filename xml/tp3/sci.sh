#!/bin/bash

let varc="$1"
shift

if test $varc -eq 2 
then
echo "Preparing stuff"
java -jar -DentityExpansionLimit=0 saxGuy.jar -out etuSet.txt dblp.xml
./dblp-prof-linux2 -out ensSet.txt dblp.xml
fi

while test $# -ne 0
do

echo "text with: " \"$1\"

if test $varc -eq 1 
then
java -jar -DentityExpansionLimit=0 saxGuy.jar -name "$1" dblp.xml | sort > etu.txt &&
./dblp-prof-linux2 -name "$1" dblp.xml | sort > ens.txt &&
diff etu.txt ens.txt

elif test $varc -eq 2
then
java -jar -DentityExpansionLimit=0 saxGuy.jar -name "$1" -in etuSet.txt | sort > etu.txt &&
./dblp-prof-linux2 -name "$1" -in ensSet.txt | sort > ens.txt &&
diff etu.txt ens.txt
fi


test $? -ne 0 && exit 127

shift
done

echo "Job DONE, GG my dude!"
