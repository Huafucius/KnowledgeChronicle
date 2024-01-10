# GCD与LCM算法

## GCD（递归）

```c
int GCD(int a, int b) {
    return a % b == 0 ? b : GCD(b, a % b);
}
```

## GCD(迭代)

```c
int GCD(int a, int b) {
    int temp;
    while (a % b != 0) {
        temp = a;
        a = b;
        b = temp % b;
    }
    return b;
}
```

## LCM

```c
int LCM(int a, int b) {
    return a * b / GCD(a, b);
}
```