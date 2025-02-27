# x64 版本的“你好，世界！”

本节讨论在 Windows 和 Linux 平台下编写 64 位的最简汇编程序，调用操作系统接口输出“你好，世界！”（不调用 C 库函数，仅使用操作系统提供的接口）。

## Windows 下的最简“你好，世界！”汇编程序

对于 64 位 Windows 应用程序，在编制汇编程序时需要遵循如下规范：

- 16 字节栈边界对齐规则
- 函数调用约定

在 Windows x64 汇编程序中使用栈空间时，在 prologs 和 leaf functions 以外的区域都需要严格保证 `rsp` 的值是 16 的整数倍。

调用函数时，需要遵循 Windows x64 调用约定。
自左向右的前四个函数参数依次送入 `rcx`、`rdx`、`r8`、`r9`，其余参数在按自右向左的顺序
依次压栈。
这里有一个极其重要的细节，在寄存器中传递的参数，**必须也在栈中为其保留相应的 32 字节空间**，这被称作 **register home**，函数在运行过程中随时有可能将 register home 用于暂存寄存器参数，或作其他用途。因此，如果没有为寄存器参数预留这部分空间，轻则调用方的数据被修改，重则因函数返回地址被修改导致函数返回时因返回到不正确的地址造成程序崩溃。

依照上述规则编写的代码如下：

```nasm
global mainCRTStartup
extern GetStdHandle
extern WriteFile
extern ExitProcess
extern GetLastError
extern Sleep
section .text
mainCRTStartup:
	push rbp ; 16-byte alignment
	mov rbp, rsp

	sub rsp, dword 4 * 8 ; home for four register parameters
	mov ecx, dword -11 ; nStdHandle = STD_OUTPUT_HANDLE
	call GetStdHandle
	add rsp, dword 4 * 8

	sub rsp, dword 6 * 8
	mov rcx, rax ; hFile
	mov rdx, qword string ; lpBuffer，此处 qword 不能省略
	mov r8d, dword STRING_SIZE ; nNumberOfBytesToWrite
	mov r9d, dword 0 ; lpNumberOfBytesWritten，对于非 Windows 7 可以为 NULL
	mov qword [rsp + 4 * 8], dword 0 ; lpOverlapped，在栈上传递
	call WriteFile

	mov rsp, rbp
	pop rbp
	ret
section .data
string:
    db "你好，世界！", 0 ; 控制台代码页需要设置为 UTF-8
    STRING_SIZE equ $ - string
```

需要指出，`mov rdx, qword string` 中的 `qword` 绝对不能省略。
其原因在于 x64 指令集中存在这样两条指令：

| 指令 | 描述 |
|---|---|
| `mov r64, imm64` | 将立即数 `imm64` 存入寄存器 `r64` |
| `mov r/m64, imm32` | 将立即数 `imm32` 进行有符号扩展后存入寄存器 `r64` 或 内存 `m64` |

x64 指令集默认的操作数大小为 32 位，因此在不指定 `qword` 时，对于这种操作数大小有多种可能的情况，操作数大小均被默认为 32 位，所以要加上 `qword` 以存入 64 位的地址。

鉴于我们没有用到 C 标准库函数，因此可以将函数入口直接指定为 `mainCRTStartup`（Win32 程序的默认入口）。

还需要注意的一点是 `STRING_SIZE` 并不是字符串中字符的个数。要计算字符串所占大小，需要用到伪指令 `equ`。

```powershell
nasm test.asm -f win64 -o test.obj
lld-link test.obj libkernel32.a /subsystem:console /out:test.exe # MSYS2 提供的工具链，链接到 libkernel32.a
```