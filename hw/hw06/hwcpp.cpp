#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

// 链表节点定义
struct ListNode {
    int value;          // 存储数字的值
    ListNode* next;     // 指向下一个节点
    ListNode(int val) : value(val), next(nullptr) {}
};

// 链表表示大整数
class BigInteger {
private:
    ListNode* head;  // 链表头
    bool isNegative; // 标记是否为负数

    // 辅助函数：清理链表
    void clear() {
        ListNode* current = head;
        while (current) {
            ListNode* temp = current;
            current = current->next;
            delete temp;
        }
        head = nullptr;
    }

public:
    BigInteger() : head(nullptr), isNegative(false) {}

    // 析构函数
    ~BigInteger() {
        clear();
    }

    // 从字符串构造大整数
    BigInteger(const string& str) {
        clear();
        isNegative = (str[0] == '-');
        int start = isNegative ? 1 : 0;
        for (int i = str.length() - 1; i >= start; i -= 3) {
            int val = 0;
            for (int j = max(start, i - 2); j <= i; ++j) {
                val = val * 10 + (str[j] - '0');
            }
            ListNode* node = new ListNode(val);
            node->next = head;
            head = node;
        }
    }

    // 显示大整数
    void print() const {
        if (isNegative) cout << "-";
        ListNode* current = head;
        bool first = true;
        while (current) {
            if (!first) {
                printf("%03d", current->value);
            } else {
                printf("%d", current->value);
                first = false;
            }
            current = current->next;
        }
        cout << endl;
    }

    // 加法运算
    BigInteger operator + (const BigInteger& other) const {
        if (isNegative == other.isNegative) {
            // 同符号相加
            BigInteger result;
            result.isNegative = isNegative;
            ListNode* p1 = head;
            ListNode* p2 = other.head;
            int carry = 0;
            while (p1 || p2 || carry) {
                int sum = carry;
                if (p1) {
                    sum += p1->value;
                    p1 = p1->next;
                }
                if (p2) {
                    sum += p2->value;
                    p2 = p2->next;
                }
                carry = sum / 1000;
                result.append(sum % 1000);
            }
            return result;
        } else {
            // 不同符号相加，转换为减法问题
            if (isNegative) {
                BigInteger temp = *this;
                temp.isNegative = false;
                return other - temp;
            } else {
                BigInteger temp = other;
                temp.isNegative = false;
                return *this - temp;
            }
        }
    }

    // 减法运算
    BigInteger operator - (const BigInteger& other) const {
        if (isNegative == other.isNegative) {
            // 同符号相减，取绝对值较大的减去较小的
            if (*this >= other) {
                BigInteger result;
                result.isNegative = isNegative;
                ListNode* p1 = head;
                ListNode* p2 = other.head;
                int borrow = 0;
                while (p1 || p2 || borrow) {
                    int diff = borrow;
                    if (p1) {
                        diff += p1->value;
                        p1 = p1->next;
                    }
                    if (p2) {
                        diff -= p2->value;
                        p2 = p2->next;
                    }
                    if (diff < 0) {
                        diff += 1000;
                        borrow = -1;
                    } else {
                        borrow = 0;
                    }
                    result.append(diff);
                }
                return result;
            } else {
                BigInteger result = other - *this;
                result.isNegative = !isNegative;
                return result;
            }
        } else {
            // 不同符号相减，转换为加法
            BigInteger temp = other;
            temp.isNegative = !temp.isNegative;
            return *this + temp;
        }
    }

    // 辅助函数：向链表添加一个数字
    void append(int val) {
        ListNode* node = new ListNode(val);
        node->next = head;
        head = node;
    }

    // 比较两个大整数的大小
    bool operator >= (const BigInteger& other) const {
        if (isNegative && !other.isNegative) return false;
        if (!isNegative && other.isNegative) return true;

        // 如果符号相同，比较绝对值
        ListNode* p1 = head;
        ListNode* p2 = other.head;
        int len1 = 0, len2 = 0;
        while (p1) { len1++; p1 = p1->next; }
        while (p2) { len2++; p2 = p2->next; }

        if (len1 > len2) return !isNegative;
        if (len1 < len2) return isNegative;

        // 如果长度相同，逐位比较
        p1 = head;
        p2 = other.head;
        while (p1 && p2) {
            if (p1->value > p2->value) return !isNegative;
            if (p1->value < p2->value) return isNegative;
            p1 = p1->next;
            p2 = p2->next;
        }
        return true;
    }
};

int main() {
    string str1, str2;
    cout << "请输入第一个大整数：";
    cin >> str1;
    cout << "请输入第二个大整数：";
    cin >> str2;

    BigInteger num1(str1), num2(str2);
    cout << "第一个大整数: ";
    num1.print();
    cout << "第二个大整数: ";
    num2.print();

    BigInteger sum = num1 + num2;
    cout << "加法结果: ";
    sum.print();

    BigInteger diff = num1 - num2;
    cout << "减法结果: ";
    diff.print();

    return 0;
}
