sleep 10
TESTDATE=$(date  +%Y-%m-%d)

file_1="/home/pi/data/cpu_stats.csv"
file_2="/home/pi/data/proc_stats.csv"


zipfile_1="/home/pi/data/zips/cpu_${TESTDATE}.zip"
zipfile_2="/home/pi/data/zips/proc_${TESTDATE}.zip"

gzip -c $file_1 > $zipfile_1
gzip -c $file_2 > $zipfile_2

rm -f $file_1
rm -f $file_2
