# [USACO17JAN] Secret Cow Code S

## 题面翻译

奶牛正在试验秘密代码，并设计了一种方法来创建一个无限长的字符串作为其代码的一部分使用。

给定一个字符串，对字符串进行一次操作（每一次正确的操作，最后一个字符都会成为新的第一个字符），然后把操作后的字符串放到操作前的字符串的后面。也就是说，给定一个初始字符串，之后的每一步都会增加当前字符串的长度。

给定初始字符串和 $N$，请帮助奶牛计算无限字符串中位置为 $N$ 的字符。

第一行输入一个字符串。该字符串包含最多 $30$ 个大写字母，数据保证 $N \leq 10^{18}$。

第二行输入 一个整数 $N$。请注意，数据可能很大，放进一个标准的 $32$ 位整数容器可能不够，所以你可能要使用一个 $64$ 位的整数容器（例如，在 C/C++ 中是 `long long`）。

请输出从初始字符串生成的无限字符串中的下标为 $N$ 的字符。第一个字符的下标是 $N=1$。

感谢 @y\_z\_h 的翻译

## 题目描述

The cows are experimenting with secret codes, and have devised a method for creating an infinite-length string to be used as part of one of their codes.

Given a string $s$, let $F(s)$ be $s$ followed by $s$ "rotated" one character to the right (in a right rotation, the last character of $s$ rotates around and becomes the new first character). Given an initial string $s$, the cows build their infinite-length code string by repeatedly applying $F$; each step therefore doubles the length of the current string.


Given the initial string and an index $N$, please help the cows compute the character at the $N$th position within the infinite code string.

## 输入格式

The input consists of a single line containing a string followed by $N$. The string consists of at most 30 uppercase characters, and $N \leq 10^{18}$.

Note that $N$ may be too large to fit into a standard 32-bit integer, so you may want to use a 64-bit integer type (e.g., a "long long" in C/C++).

## 输出格式

Please output the $N$th character of the infinite code built from the initial string. The first character is $N=1$.

## 样例 #1

### 样例输入 #1

```
COW 8
```

### 样例输出 #1

```
C
```

## 提示

In this example, the initial string COW expands as follows:


COW -> COWWCO -> COWWCOOCOWWC

12345678

## 题解

### 题目分析

这是一道递归题目。首先观察数据规模，长度为 $10^18$ 的字符串，就算线性遍历一遍也不可能了。所以一定不是从前往后、从小往大地生成数据，一定是对数级别的算法。

于是我们考虑从后往前逆推，也就是找到字符串生成的逆过程，它怎么生成，就怎么把它还原回去。换句话说，我们找到第n个字符的“来源”位置，由于每次生成字符串长度都翻倍，所以每次逆生成字符串长度都减半。并且，我们只关注第n个字符的下标来源，不需要去处理具体的字符。

首先我们找到字符串长度`len`，然后计算出最终字符串的长度`temp_len`，并让它减半。我们可以把最终字符串看作是由`temp_len`长度的字符串生成而来。如果`n=temp_len+1`，根据特殊的规则，第一个字符是重复的，`n=temp_len` 。其它情况下，易知`n=n-(temp_len+1)`。

### AC代码

```c++
#include<iostream>
#include<string>
using namespace std;

string str;  // 原始字符串
long long n; // 字符位置n
long long len, temp_len; // 原始长度len和逆生成过程中的长度temp_len

int main() {
	cin >> str >> n;
	len = str.length();

	// 只要n还大于len，就要继续逆生成
	while (len < n) {
		// 计算逆生成字符串长度temp_len，每次都要重新算
		temp_len = len;
		while (temp_len < n) temp_len <<= 1;
		temp_len >>= 1;

		// 进行下标的逆生成，根据题意有两种情况分类讨论
		if (n == temp_len + 1)
			n -= 1;
		else
			n = n - (temp_len + 1);
	}

	cout << str[n-1];
}
```

### WA代码

WA了好几次，还有TLE，分别是下面几个错误：

**人家n是从1开始，数组下标是从0开始，忘了减一。**

```c++
cout << str[n];
```

**if里面写了个赋值符号。**

```c++
if (n = temp_len + 1)
n -= 1;
else
n = n - temp_len - 1;
```

**因为n可能一步到位，所以temp_len并不是每次除二，而是需要每次单独重新赋值计算。**

```c++
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

string str;
long long n;
int len, temp_len;

int main() {
	cin >> str >> n;
	len = temp_len = str.length();
	while (temp_len < n) temp_len <<= 1; // 这里不应该放到外面，应该在while循环里面

	while (len < n) {
		temp_len >>= 1;

		if (n == temp_len + 1)
			n -= 1;
		else
			n = n - temp_len - 1;
	}

	cout << str[n-1];
}
```
