#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

// ����ڵ㶨��
struct ListNode {
    int value;          // �洢���ֵ�ֵ
    ListNode* next;     // ָ����һ���ڵ�
    ListNode(int val) : value(val), next(nullptr) {}
};

// �����ʾ������
class BigInteger {
private:
    ListNode* head;  // ����ͷ
    bool isNegative; // ����Ƿ�Ϊ����

    // ������������������
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

    // ��������
    ~BigInteger() {
        clear();
    }

    // ���ַ������������
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

    // ��ʾ������
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

    // �ӷ�����
    BigInteger operator + (const BigInteger& other) const {
        if (isNegative == other.isNegative) {
            // ͬ�������
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
            // ��ͬ������ӣ�ת��Ϊ��������
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

    // ��������
    BigInteger operator - (const BigInteger& other) const {
        if (isNegative == other.isNegative) {
            // ͬ���������ȡ����ֵ�ϴ�ļ�ȥ��С��
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
            // ��ͬ���������ת��Ϊ�ӷ�
            BigInteger temp = other;
            temp.isNegative = !temp.isNegative;
            return *this + temp;
        }
    }

    // �������������������һ������
    void append(int val) {
        ListNode* node = new ListNode(val);
        node->next = head;
        head = node;
    }

    // �Ƚ������������Ĵ�С
    bool operator >= (const BigInteger& other) const {
        if (isNegative && !other.isNegative) return false;
        if (!isNegative && other.isNegative) return true;

        // ���������ͬ���ȽϾ���ֵ
        ListNode* p1 = head;
        ListNode* p2 = other.head;
        int len1 = 0, len2 = 0;
        while (p1) { len1++; p1 = p1->next; }
        while (p2) { len2++; p2 = p2->next; }

        if (len1 > len2) return !isNegative;
        if (len1 < len2) return isNegative;

        // ���������ͬ����λ�Ƚ�
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
    cout << "�������һ����������";
    cin >> str1;
    cout << "������ڶ�����������";
    cin >> str2;

    BigInteger num1(str1), num2(str2);
    cout << "��һ��������: ";
    num1.print();
    cout << "�ڶ���������: ";
    num2.print();

    BigInteger sum = num1 + num2;
    cout << "�ӷ����: ";
    sum.print();

    BigInteger diff = num1 - num2;
    cout << "�������: ";
    diff.print();

    return 0;
}
