#include <iostream>
#include <cmath>
using namespace std;

double f(double x);
double ff(double x);
int main()
{
    ///fx = x^2 - 5
    ///ff = 2x
	double xnew;
    double xold = -50000;
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
	double e = 2.71828182846;
    x = x-pow(e,-1*pow(x,2));
    return x;
}
double ff(double x)
{
	double e = 2.71828182846;
	x = (2*x)/(pow(x,2)) + 1;
    return x;
}