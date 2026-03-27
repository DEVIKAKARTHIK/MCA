while true
do
read -p "enter the values" a b
read -p "enter the operator" op
case $op in 
"+")
    echo "result: $((a+b))";;
"-")
    echo "result: $((a-b))";;
"*")
    echo "result: $((a*b))";;
"/")
    echo "result: $((a/b))";;
esac
done