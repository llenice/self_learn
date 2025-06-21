#include<iostream>
using namespace std;
//void f(int a[]){}
int main() {
    //int a[3];
    int a[3] [3]= {0};
    cout << a <<" "<<a + 1 << endl; //  12                                                a+1 +了sizeof(int[3])
    cout <<&a<<" "<< &a + 1 <<endl; //36
    cout<<*a<<" "<<*a+1<<endl;    //4
    cout<<*&a<<" "<<*&a+1<<endl;
    
}