section .data
    msg db 'Madre mía, cómo me gusta la asignatura de ENTORNOS DE DESARROLLO 😊', 0

section .text
    global _start

_start:
    ; syscall write(1, msg, len)
    mov rax, 1                  ; syscall número 1 - write
    mov rdi, 1                  ; file descriptor 1 - stdout
    mov rsi, msg                ; dirección del mensaje
    mov rdx, 64                 ; longitud del mensaje (sin incluir el NULL)
    syscall                     ; llamar al sistema para escribir

    ; syscall exit(0)
    mov rax, 60                 ; syscall número 60 - exit
    xor rdi, rdi                ; código de salida 0
    syscall                     ; llamar al sistema para salir
