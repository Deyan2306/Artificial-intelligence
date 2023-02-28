; The code is a Linux-compatible version!

section .text
    global _start

section .data
msg db 'Welcome to my world!', 0xa
len equ $ - msg

section .text

_start:
    mov edx, len
    mov ecx, msg
    mov ebx, 1
    mov eax, 4
    int 0x80 ;call kernel

    mov ebx, 0
    mov eax, 1
    int 0x80