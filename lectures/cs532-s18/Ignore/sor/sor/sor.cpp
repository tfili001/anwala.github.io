#ifndef SOR_H_INCLUDED
#define SOR_H_INCLUDED
#include "matrix.h"
#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;



void sor(int n)
{

    double **A = randomizeMat(createMat(n),n);
    double  *b = createRandVec(n);
    double  *x = createVec(n);
    double  *xold = createVec(n);
	double  rel = 1.0;
	for(int i =0;i<n;i++)
	{
		xold[i]=0;
		x[i]=0;
	}
	cout<<"Size       = "<<n<<endl
		<<"Relaxation = "<<rel<<endl;
	
	
	
    for(int k=0;k<n;k++)
    {
        for(int i=0;i<n;i++)
        {	
			double sum1=0.0;
			double sum2=0.0;

			for(int j=0;j<i;j++)
			{
			//if(i!=j)
			//xold[j]=x[j];

				sum1+=(A[i][j]*x[j]);


			}
			for(int j=i;j<n;j++)
			{
				
			xold[j]=x[j];

			if(i!=j)

				sum2+=(A[i][j]*xold[j]);


			}
			cout<<"index = "<<i<<endl;
			
		 x[i]=(rel/A[i][i])*(b[i]-sum1-sum2)+(1-rel)*xold[i];
			/*for(int a=0;a<n;a++)
			{
				xold[a]=x[a];
			}
			 * */
		}
		cout<<"remove iterate\n";
	 
    }
	/***End of SOR***/

	
	

	

	 
	 cout<<"A matrix\n";
	 display(A,n);
	 
	 cout<<"x vector\n";
	 printVec(x,n);
	 
	 cout<<"xold vector\n";
	 printVec(xold,n);
	 
	 errorNorm(b,A,x,n);

/*** Cleanup ***/
  removeMat(A,n);
  delete b;
  delete x;
  delete xold;
}

  

int main(){
	
	int n = 20;
	sor(n);
return 0;
}

#endif // SOR_H_INCLUDED
