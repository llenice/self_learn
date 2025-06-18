#include<iostream>
#include<algorithm>
using namespace std;
struct a
{
    float y;
    short int x;
    char code[3];
}k;
int mode(int a[],int n)
{
    for (int i = 0; i < n; i++)
    {
        if(a[0]<a[i])
        {
            swap(a[i],a[0]);
        }        
    }   
    int cnt[a[0]]={0};
    for (int i = 0; i < n; i++)
    {
        cnt[a[i]]++;
    }
    int k=0;
    for (int i = 1; i < a[0]; i++)
    {
        if(cnt[i]>cnt[k])
        {
            k=i;
        }
        //cout<<cnt[i]<<" ";       
    }
    return k;   
}
int main(){
    char a[10], *p=a;
}