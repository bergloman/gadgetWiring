#tail -n +8 out.txt | awk '{printf "%s,%s,%.2f,%.2f\n",$(12),$(2), $(9), $(10)}'


NOW=$(date -Is)
top -bn1 | tail -n +8 | awk '{printf ",%s,%s,%.2f,%.2f\n",$(12),$(2), $(9), $(10)}' | awk -v now=$NOW '{print now$0}'

