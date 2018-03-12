#include <iostream>
#include <iomanip>
#include <random>
#include <ctime>
using namespace std;

double rangen()
{
  static default_random_engine generator;
  uniform_real_distribution<double> distribution (-100,100);
  return distribution(generator);	
}

void display(double **A,int n){
	cout<<"____________________\n";

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
        cout<<setw(8)<<setprecision(4)<<A[i][j];
        }
     cout<<endl;
    }
}

double *createSol(int n){
	double *sol = new double[n];
	
	for(int i=0;i<n;i++)
	{
		double a=rangen();
		if(a<0)
		{
		a*=(-1);
		}
	sol[i]=a;
	cout<<sol[i]<<endl;
	}	
return sol;
}

double **createMat(int n){

    double sum;
    double **A;

    A = new double *[n];
///Have each of the new pointers point at a vector of size t
    for(int i=0; i<n; i++)
    {
        A[i]=new double[n];
    }

///Fill in the matrix
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
		A[i][j]=rangen();
        }
    }
	display(A,n);

///Set entries absolute
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
        if(A[i][j]<0)
           A[i][j]*=(-1);
        }
    }

///Set diagonals to zero
    
    for(int i=0; i<n; i++)
    {
        A[i][i]=0;
    }
	
///Diagonally dominant
	for(int i=0; i<n; i++)
	{
        for(int j=0; j<n; j++)
        {
		sum+=A[i][j];
        }
	A[i][i]=sum;
	sum=0;
    }

	display(A,n);
	
return A;
}

double *getB(double **A,double *sol,int n){
	double *B = new double[n];
	
	for(int i=0;i<n;i++)
	{	
		for(int j=0;j<n;j++)
		{
			B[i]+=(A[i][j])*(sol[j]);
		}
	}
	cout<<"B vector\n";
	for(int i=0;i<n;i++)
	{
		cout<<fixed<<B[i]<<endl;
	}
	
return B;
}
void gauss(double **A,int n)
{
	for(int i=0;i<n;i++)
	{   double multp = 1/A[i][i];
		for(int j=0;j<n;j++)
		{
			A[i][j]*=multp;
			for(int k=j;k<n;k++)
			{
				A[k][j-1]=A[j][j]*A[k][j-1]-A[k][j-1];
			}
			
		}
	}
	display(A,n);
}

void getInv(double **A,int m)
{
	int n = 2*m;
	double **Tmp = new double *[n];///should be   M
	for(int a=0; a<n; a++)
    {
        Tmp[a]=new double[n];
    }
/*
	for(int i=0;i<m;i++)
	{

		for(int j=0;j<n;j++)
		{
			cout<<"m:"<<m<<" i:"<<i<<" j:"<<j<<endl;
			
			Tmp[i][j]=A[i][j];
		}
	
	
	}
	*/
	for(int i=0;i<n;i++)
	{
		for(int j=m;j<n;j++)
		{
			if(i==j)
				Tmp[j][j]=1;
			else
				Tmp[i][j]=0;
		}
	}
		
	for(int i=4;i<n;i++)
	{
	}


	
	
	cout<<"Display________________________________\n";	
	for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
        cout<<setw(8)<<setprecision(4)<<fixed<<Tmp[i][j];
        }
     cout<<endl;
    }
	 
}



int main()
{
    int n;
    cout<<"What size?"<<endl;
    cin>>n;
	
    double **A  = createMat(n);
	double *sol = createSol(n);
  ///  double *B   = getB(A,sol,n);
///	gauss(A,n);
	getInv(A,n);

return 0;
}

