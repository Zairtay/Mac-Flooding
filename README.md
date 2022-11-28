/!\ The purpose here is for educational use only, I am not responsible for what you do with this script. /!\


# Mac-Flooding
This tool will allow you to spam the content addressable memory of your switch or router to fill the busy ports. The router or switch will then broadcast to all ports.


Before installing :

-pip install rstr
-pip install scapy[basic]

For running : 

```
user@kali>python3 MacFlooding.py ${IP OF VICTIM}
```

Exemple with my router ( PfSense virtual machine ) : 

```
user@kali>python3 MacFlooding.py 192.168.1.1
```

