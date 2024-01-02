//高精度加法
void highPrecisionAdd(char *num1, int lenNum1, char *num2, int lenNum2, char *result) {
    int carry = 0;  // 进位
    int i = 0;      // 当前处理的位置

    // 遍历两个数的每一位，直到最高位处理完毕
    for (i = 0; i < lenNum1 || i < lenNum2 || carry; i++) {
        if (i < lenNum1) {
            carry += num1[i] - '0';
        }
        if (i < lenNum2) {
            carry += num2[i] - '0';
        }

        // 计算当前位并考虑之前的进位
        result[i] = (carry % 10) + '0';

        // 计算新的进位
        carry /= 10;
    }

    // 字符串以'\0'结束
    result[i] = '\0';
}

//高精度乘法
void highPrecisionMultiply(char *n, int len_n, char *m, int len_m, char *result) {
    for (int i = 0; i < len_n; i++) {
        for (int j = 0; j < len_m; j++) {
            int digit = (n[i] - '0') * (m[j] - '0') + result[i + j];
            result[i + j] = digit % 10;
            result[i + j + 1] += digit / 10;
        }
    }
    for (int i = 0; i < len_n + len_m; i++)
        result[i] += '0';
    result[len_n + len_m] = '\0';
}
