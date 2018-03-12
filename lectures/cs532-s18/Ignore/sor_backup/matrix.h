#ifndef MAT_H_INCLUDED
#define MAT_H_INCLUDED
#include <iostream>
#include <iomanip>
#include <random>
#include <ctime>
#include <cmath>
using namespace std;
void display(double **A,int m,int n){
    cout<<"_____________________\n";
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
        cout<<setw(8)<<setprecision(4)<<A[i][j]<<" ";
        }
     cout<<endl;
    }
}
void display(double **A,int n){
    for(int i=0;i<n;i++){
    cout<<"_________";
    }
cout<<endl;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
        cout<<setw(8)<<setprecision(4)<<A[i][j]<<" ";
        }
     cout<<endl;
    }
}
void printVec(double *x,int n){
    for(int i=0; i<n; i++)
            {
            cout<<setw(8)<<setprecision(4)<<x[i]<<endl;
            }
}

double *createVec(int n)
{
    double *x = new double[n];
    for(int i=0;i<n;i++)
    {
        x[i]=0;
    }

    return x;
}
int seed = time(0);
default_random_engine engine(seed);

double *createRandVec(int n)
{
    uniform_real_distribution<double> dist (-100,100);

    double *x = new double[n];
    for(int i=0;i<n;i++)
    {
        x[i]=dist(engine);
    }

    return x;
}

double **createMat(int n){
    double **A;
    A = new double *[n];
    int sum;
    for(int i=0; i<n; i++)
    {
        A[i]=new double[n];
    }
    for(int i=0; i<n; i++)
	{
        for(int j=0; j<n; j++)
        {
		sum+=A[i][j];
        }
	A[i][i]=sum*10;
	sum=0;
    }

    return A;
}



double **randomizeMat(double **A,int n)
{
    uniform_real_distribution<double> dist (-100,100);
    double sum=0;

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
		A[i][j]=dist(engine);
        }
    }

///Set entries absolute
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
        if(A[i][j]<0)
           A[i][j];
        }
    }
	for(int i=0; i<n; i++)
	{
        for(int j=0; j<n; j++)
        {
		sum+=A[i][j];
        }
	A[i][i]=sum*10;
	sum=0;
    }
return A;
}


#endif // MAT_H_INCLUDED