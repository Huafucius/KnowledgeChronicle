# n皇后问题

## 题目描述

## 题解

### AC代码

```c
#include<stdio.h>
#include<math.h>
#include<malloc.h>

// 全局变量，用于存储符合条件的解的数量
int count = 0;

/**
 * 打印一个解的函数
 * path[] 存储皇后的列位置
 * n 棋盘的大小
 */
void printSolution(int* path, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // 如果第 i 行的皇后放在第 j 列，打印 'Q'，否则打印 '.'
            if (path[i] == j)
                printf("Q ");
            else
                printf(". ");
        }
        printf("\n");
    }
    printf("\n");
}

/**
 * 判断在 line 行 column 列是否能放置皇后
 * path[] 存储已放置的皇后的位置
 * line 当前行
 * column 当前列
 * 返回值：如果可以放置则返回 true，否则返回 false
 */
int isSafe(int* path, int line, int column) {
    for (int i = 0; i < line; i++) {
        // 检查列和对角线是否有冲突
        if (path[i] == column || abs(path[i] - column) == abs(i - line))
            return 0;
    }
    return 1;
}

/**
 * 递归函数来放置皇后
 * path[] 存储皇后的位置
 * line 当前处理的行
 * n 棋盘的大小
 */
void placeQueen(int* path, int line, int n) {
    if (line == n) {
        printSolution(path, n);
        count++;
        return;
    }

    for (int i = 0; i < n; i++) {
        if (isSafe(path, line, i)) {
            path[line] = i;
            placeQueen(path, line + 1, n);
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);

    int* path = (int*)malloc(sizeof(int) * n);
    placeQueen(path, 0, n);
    printf("\n总共有 %d 种解法。\n", count);
    return 0;
}

```
