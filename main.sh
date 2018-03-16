name=$(ip link | grep -E "(wl|mon)" | cut -f2 -d':' | sed 's/ //g')
adapter="$name"
if [[ `echo $name | wc -l` -ge 1 ]]; then
  echo "Choose an adapter:"
  for i in $name; do
    echo $i
  done
fi
python p.py $name
