# Value Categories

There are three types of value in C++: lvalue, xvalue, and prvalue. We'll explore these three types in this article.

## The `Has` Property

Naturally, when we define a variable in C++, that variable holds a value. For example, the following C++ statement defines a variable named `a`.

```C++
int a{ 100 };
```

This C++ statement corresponds to the assembly instruction below:

```asm
push dword 100
```

The above x86 assembly instruction will be assembled into the following machine code, and we can see that the integer `100` is represented in its hexadecimal form `64`:

```text
6A66 0064
```

Obviously, `a` as a variable, is actually an alias for a block of memory in the program stack, and we have full control over this block of memory, meaning we can either read from or write to this memory block. In such cases, we say `a` *has* an *entity*, and this entity is where the value `100` will be stored.

However, not all values are stored in memory blocks we can have full control over. Before `100`, the integer literal in the above statement, are stored in the memory block aliased by `a`, already exists in the compiled code as an inherent part of the x86 instruction `6A66 0064`. Even though this instruction is stored in memory when the operating system loads the program, we cannot change the hexadecimal `64` to some other value since the operating system forbids us from writing to `.text` section, i.e., the memory section where program instructions is placed. Then, we can conclude that we cannot change literals present in our C++ program. We cannot write something like:

```C++
100 = 101; // error: assign 101 to literal 100
```

Then, we say that the literal `100` does not have an entity.

## The `Move` Property

Let's delve into the above example. `a` is bound to a block of memory which we have full control over. On this basis, we say `a` *has* that *entity*. As programmers, we cannot deprive `a` of its entity, i.e., delete `a` and binds its associated memory block to another symbol. Therefore, we say `a`'s memory cannot be moved. We often say that `a` is non-moveable for simplicity.

There do exist cases in which we can move entities refered by a symbol, of which the simplest case is literals. Since literals does not have associated entities and thus cannot be modified, we can "move" them to anywhere. Such "move" is more like "copy" rather than change an object's place. Anyone can claim that they get the ownership of a literal as long as they promise not to change their value. Some compilers may allow us to take the ownership of a literal without such promise, but will give us an error. If we try to change that literal through this problematic owership claim, the operating system will have our program crashed at run-time.

```C++
const char* s1 = "hello"; // ok, promise not to change a literal's value
char* s2 = "hello"; // warning: cannot assign const char* to char*
s2[0] = "H"; // will case a runtime error
```

Another case in which we can move is when the C++ runtime creates temporary objects. Different from literals, such temporary objects are usually moveable.

```C++
std::string s3 = "Hello";
s3 + "World" = "hello, world";
```

The above example first constructs a string object `s3`, then we concatenate `s3` with a string literal `"World"`, during which a temporary string object containing value `"HelloWorld"` will be created, i.e., such concatenation is equivalent to the following code:

```C++
std::string temp = "HelloWorld";
temp = "hello, world";
```

Obviously, `temp` as a temporary object, will be held by nobody after the concatenation and assignment operations complete and will be destructed automatically. An natural idea comes that we can take the ownership of such a will-be destructed object, and such idea is the core of move semantics introduced in C++ 11.

## Value Categories

Based on "Has" and "Move" property of a value, we can classify C++ values into three categoried.

<table>
    <tr>
        <th>Has</th><th>Move</th><th>Category</th><th>Example</th>
    </tr>
    <tr>
        <td>yes</td><td>no</td><td><b>lvalue</b></td><td>Ordinary variables</td>
    </tr>
    <tr>
        <td>yes</td><td>yes</td><td><b>xvalue</b></td><td>Temporary Unnamed Objects</td>
    </tr>
    <tr>
        <td>no</td><td>yes</td><td><b>prvalue</b></td><td>Literals</td>
    </tr>
</table>

Since both lvalues and xvalues have associated entities and thus can be modified, people define another more gneralized category — **glvalue** (general lvalue) to refer to any value that has an associated entity. Likewise, since both xvalues and prvalues are held by nobody, people define a category named **rvalue** to refer to any moveable value.