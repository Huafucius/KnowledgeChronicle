# [USACO1.2] 方块转换 Transformations

## 题目描述

一块 $n \times n$ 正方形的黑白瓦片的图案要被转换成新的正方形图案。写一个程序来找出将原始图案按照以下列转换方法转换成新图案的最小方式：

- 转 $90\degree$：图案按顺时针转 $90\degree$。

- 转 $180\degree$：图案按顺时针转 $180\degree$。

- 转 $270\degree$：图案按顺时针转 $270\degree$。

- 反射：图案在水平方向翻转（以中央铅垂线为中心形成原图案的镜像）。

- 组合：图案在水平方向翻转，然后再按照 $1 \sim 3$ 之间的一种再次转换。

- 不改变：原图案不改变。

- 无效转换：无法用以上方法得到新图案。

如果有多种可用的转换方法，请选择序号最小的那个。

只使用上述 $7$ 个中的一个步骤来完成这次转换。

## 输入格式

第一行一个正整数 $n$。   

然后 $n$ 行，每行 $n$ 个字符，全部为 `@` 或 `-`，表示初始的正方形。

接下来 $n$ 行，每行 $n$ 个字符，全部为 `@` 或 `-`，表示最终的正方形。

## 输出格式

单独的一行包括 $1 \sim 7$ 之间的一个数字（在上文已描述）表明需要将转换前的正方形变为转换后的正方形的转换方法。

## 样例 #1

### 样例输入 #1

```
3
@-@
---
@@-
@-@
@--
--@
```

### 样例输出 #1

```
1
```

## 提示

【数据范围】  
对于 $100\%$ 的数据，$1\le n \le 10$。

题目翻译来自 NOCOW。

USACO Training Section 1.2

## 题解

这是我做的第一道提高题（虽然是提高-），但仍旧十分具备纪念性质！咱们才不管什么算法呢，直接模拟七种情况，把方阵转过来，然后再谈比较的事情。因为当时刚刚接触C语言不久，所以代码十分的青涩，调试了不知道多久，最后甚至直接上C++（好像是为了偷懒不想用标准输入？）。好在最后还是过了，而且是在没有借助外力的情况下第一道独立的提高-！可喜可贺，可喜可贺！

重点在于搞明白方阵各种旋转镜像操作对于坐标的影响，这里用GPT总结如下：

### 矩阵变换对坐标的影响

1. **顺时针旋转90度（Rotate 90° Clockwise）**
   - 新的 `x` 坐标变为原来的 `y` 坐标。
   - 新的 `y` 坐标变为 `n - x + 1`。
   - 转换公式：`(x, y) → (y, n - x + 1)`。

2. **顺时针旋转180度（Rotate 180° Clockwise）**
   - 新的 `x` 坐标变为 `n - x + 1`。
   - 新的 `y` 坐标变为 `n - y + 1`。
   - 转换公式：`(x, y) → (n - x + 1, n - y + 1)`。

3. **顺时针旋转270度（Rotate 270° Clockwise）**
   - 新的 `x` 坐标变为 `n - y + 1`。
   - 新的 `y` 坐标保持为原来的 `x` 坐标。
   - 转换公式：`(x, y) → (n - y + 1, x)`。

4. **水平镜像（Horizontal Reflection）**
   - `x` 坐标保持不变。
   - `y` 坐标变为 `n - y + 1`。
   - 转换公式：`(x, y) → (x, n - y + 1)`。

### AC代码
```c
#include<stdio.h>
#include<iostream>
using namespace std;
int main() {
    char n0[11][11] = {};
    char m0[11][11] = {};
    char r[11][11] = {};
    int condition = 1, judge = 1;
    int no_change = 0;
    int n;

    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> n0[i][j];
        }
        getchar();
    }
    //初始矩阵输入
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> m0[i][j];
        }
        getchar();
    }
    //判定矩阵输入

    for (condition; condition <= 4; condition++) {
        judge = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                r[i][n + 1 - j] = n0[j][i];
                if (r[i][n + 1 - j] != m0[i][n + 1 - j])
                    judge = 0;
            }
        }
        if (judge == 1) {
            if (condition == 4)
                no_change = 1;
            else {
                cout << condition;
                return 0;
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                n0[i][j] = r[i][j];
            }
        }
    }
    //四次旋转

    judge = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            r[i][n + 1 - j] = n0[i][j];
        }
    }
    //初始矩阵反射

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            n0[i][j] = r[i][j];
            if (r[i][j] != m0[i][j])
                judge = 0;
        }
    }
    if (judge == 1) {
        cout << 4;
        return 0;
    }
    //反射判断

    judge = 1;
    for (int k = 1; k < 4; k++) {
        judge = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                r[i][n + 1 - j] = n0[j][i];
                if (r[i][n + 1 - j] != m0[i][n + 1 - j])
                    judge = 0;
            }
        }
        if (judge == 1) {
            cout << 5;
            return 0;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                n0[i][j] = r[i][j];
            }
        }
    }
    //反射后旋转
    if (no_change == 1) {
        cout << 6;
    }
    else
        cout << 7;
    return 0;
}
```
