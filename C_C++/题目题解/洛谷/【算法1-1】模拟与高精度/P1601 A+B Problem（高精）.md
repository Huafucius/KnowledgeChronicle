# A+B Problem（高精）

## 题目描述

高精度加法，相当于 a+b problem，**不用考虑负数**。

## 输入格式

分两行输入。 $a,b \leq 10^{500}$ 。

## 输出格式

输出只有一行，代表 $a+b$ 的值。

## 样例 #1

### 样例输入 #1

```
1
1
```

### 样例输出 #1

```
2
```

## 样例 #2

### 样例输入 #2

```
1001
9099
```

### 样例输出 #2

```
10100
```

## 提示

$20\%$ 的测试数据， $0\le a,b \le10^9$ ；

$40\%$ 的测试数据， $0\le a,b \le10^{18}$ 。

## 题解

### 题目分析1

一道高精度算法（加法）的板子题，时常来看看，找到自己最喜欢的写法。

大体思路明确，给两个数组输出第三个数组，中间逢十进位即可。

### AC代码1（C风格）

```c
#include <stdio.h>
#include <string.h>

// 定义数组大小为最大的输入长度加1
#define MAX_LENGTH 505

void addBigNumbers(char num1[], char num2[], char result[]) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int carry = 0;
    int maxLen = len1 > len2 ? len1 : len2;

    for (int i = 0; i < maxLen; ++i) {
        int digit1 = i < len1 ? num1[len1 - 1 - i] - '0' : 0;
        int digit2 = i < len2 ? num2[len2 - 1 - i] - '0' : 0;
        int sum = digit1 + digit2 + carry;
        carry = sum / 10;
        result[i] = sum % 10 + '0';
    }
    if (carry) {
        result[maxLen] = carry + '0';
        result[maxLen + 1] = '\0';
    }
    else {
        result[maxLen] = '\0';
    }
    int len = strlen(result);
    for (int i = 0; i < len / 2; i++) {
        char temp = result[i];
        result[i] = result[len - 1 - i];
        result[len - 1 - i] = temp;
    }
}

int main() {
    char num1[MAX_LENGTH], num2[MAX_LENGTH], result[MAX_LENGTH + 1]; // 结果数组需要多一个位置存放字符串结束符

    // 读取输入数字
    scanf("%s %s", num1, num2);

    // 调用函数进行高精度加法
    addBigNumbers(num1, num2, result);

    // 输出结果
    printf("%s\n", result);

    return 0;
}
```

### 题目分析2

用C++的`string`来实现，通过题目熟悉`string`的一些方法。并且这次使用了为短数组添加前导0的模式，`string`可变长就是舒服。

### AC代码2（C++风格）

```c++
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

string addBigNumbers(string a, string b) {
	// 字符串反转，低位在前
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	// 初始化数据
	int len1 = a.length(), len2 = b.length();
	int max_len = max(len1, len2), len_diff = abs(len1 - len2);
	int carry = 0, digit = 0;
	string result;
	result.reserve(max_len + 1);

	// 为较短的数字填充前导0
	if (len1 < len2) a.append(len_diff, '0');
	else b.append(len_diff, '0');

	// 高精度加法主体
	for (int i = 0; i < max_len; ++i) {
		digit = a[i] - '0' + b[i] - '0' + carry;
		result.push_back(digit % 10 + '0');
		carry = digit / 10;
	}

	// 解决最后的进位
	if (carry > 0) result.push_back(carry + '0');

	reverse(result.begin(), result.end());
	return result;
}

int main() {
	string a, b;
	cin >> a >> b;
	cout << addBigNumbers(a, b);
}
```
