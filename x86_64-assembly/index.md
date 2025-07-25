---
title: x86_64 汇编
---

## 简介

这是一份 x86_64 汇编的学习记录。

一些关于**汇编怎样写**的资料：

- [AMD64 Architecture Programmer's Manual](https://docs.amd.com/v/u/en-US/40332-PUB_4.08)
- [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://cdrdv2-public.intel.com/858440/325462-088-sdm-vol-1-2abcd-3abcd-4.pdf)
- [NASM 文档](https://www.nasm.us/docs.php)

除了写汇编代码，我们还需要了解汇编与其他编程语言如何协同工作，这就涉及到 ABI （Application Binary Interface），Windows 和 Linux 有不同的 ABI 规范：

Windows ABI 的文档比较分散，一方面原因是微软并不鼓励在 Windows 下采用汇编语言编制程序，另一方面是 ABI 包含的内容太多，全都分散在在 C / C++ 文档、MSVC 编译器文档的各个角落。
不过微软还是系统地提供了一些关于调用约定等方面的文档：

- [Microsoft x86 Calling Convention](https://learn.microsoft.com/en-us/cpp/cpp/calling-conventions)
- [Microsoft x64 Calling Convention](https://docs.microsoft.com/en-us/cpp/build/x64-calling-convention)

再比如，像结构体对齐方式、Windows PE 文件格式规范等都是 Windows ABI 的一部分：

- [Alignment](https://learn.microsoft.com/en-us/cpp/c-language/alignment-c)
- [PE Format](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format)

Linux ABI 规范被称作 System V Application Binary Interface，分为 i386 版本和 AMD64 版本，其相关资料可以在 [Linux Foundation Referenced Specifications](https://refspecs.linuxbase.org/) 找到。
