#include<bits/stdc++.h>
using namespace std;

int factorial(int a)
{
    if(n==0||n==1)
        return 1;
    
    return a*factorial(a-1);
}

int main()
{
    int a=6;
     cout<<factorial(a);
    return 0;
}
