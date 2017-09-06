tail -n +8 out.txt | awk '{printf "%s,%s,%.2f,%.2f\n",$(12),$(2), $(9), $(10)}'
