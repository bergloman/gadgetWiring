import os
import os.path

# Return CPU temperature as a character string
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

# Return % of CPU used by user as a character string
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))

# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

#########################

# CPU informatiom
CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()

print CPU_temp
print CPU_usage

# RAM information
# Output is in kb, here I convert it in Mb for readability
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used = round(int(RAM_stats[1]) / 1000,1)
RAM_free = round(int(RAM_stats[2]) / 1000,1)

print RAM_total
print RAM_used
print RAM_free

# Disk information
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_free = DISK_stats[1]
DISK_perc = DISK_stats[3]

print DISK_total
print DISK_free
print DISK_perc

now_str = datetime.now().isoformat()

file_name = argv[1]


if !os.path.exists(file_name):
    hs = open(file_name, "w")
    hs.write("now,cpu_temp,cpu_usage,ram_total,ram_used,ram_free,disk_total,disk_free,disk_perc\n")
    hs.close()

hs = open(file_name, "a")

hs.write(now_str + ",")
hs.write(str(CPU_temp) + ",")
hs.write(str(CPU_usage) + ",")
hs.write(str(RAM_total) + ",")
hs.write(str(RAM_used) + ",")
hs.write(str(RAM_free) + ",")
hs.write(str(DISK_total) + ",")
hs.write(str(DISK_free) + ",")
hs.write(str(DISK_perc) + "\n")

hs.close()
