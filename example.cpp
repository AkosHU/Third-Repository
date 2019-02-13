#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
int i=0;
double k=44453;
bool b=true;
cout<<scientific<<k<<endl;
for(int j=0; j<100; j++)
{
i+=123*j+3;
if(b) {cout<<setprecision(5)<<setw(10)<<i<<" "; b=false;}
else {cout<<setprecision(5)<<setw(10)<<i<<endl;b=true;}
}
cout<<scientific<<i<<endl;
return 0;
}
