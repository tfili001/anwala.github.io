#include <iostream>
#include <cmath>
using namespace std;

double f(double x);
double ff(double x);
int main()
{
    double xold, xnew;
    xold = -50000;
    double tol = .00001;
    bool cont = true;
    int it=0;
    while(cont)
    {
       xnew = xold - (f(xold)/ff(xold));
       cout<<"New x = "<<xnew<<endl;
       if(abs(xnew-xold)<tol){cont = false;}
       xold = xnew;
       it++;
    }
    cout<<"final solution: "<<xnew<<" in "<<it<<" iterations"<<endl;
}

double f(double x)
{
    x = pow(x,3)-(2*pow(x,2))+x-3;
    return x;
}
double ff(double x)
{
    x = (3*pow(x,2))-(4*x)+1;
    return x;
}