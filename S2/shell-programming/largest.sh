echo "enter the number"
read a
echo "enter the number"
read b
echo "enter the number"
read c

if [ $a -ge $b ] && [ $a -ge $c ]; then
    echo "largest number is:$a"
elif [ $b -ge $a ] && [ $b -ge $c ]; then
    echo "largest number is:$b"
else
    echo "largest number is:$c"
fi

