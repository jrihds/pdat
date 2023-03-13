for f in $(ls *.py)
do 
   pygmentize -O full,style=borland -o ../content/$(echo $f | cut -f1 -d".").html $f
done
