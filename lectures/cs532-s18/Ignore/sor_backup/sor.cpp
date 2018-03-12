#include "matrix.h"
#include <iostream>

using namespace std;
void sor(int n){

    double **A = randomizeMat(createMat(n),n);
    double  *b = createRandVec(n);
    double  *x = createVec(n);
    double *xold = createVec(n);


    for(int k=0;k<n;k++)
    {
        for(int i=0;i<n;i++)
        {
        double sum = 0.0;
        double inv = 1/A[i][i];
            for(int j=0;j<i;j++)
            {
                sum += A[i][j]*x[j];
            }
            for(int j=i;i<n;i++)
            {
                sum += A[i][j]*xold[j];
            }
            sum = (b[i]-sum)/inv;
            for(int a=0;a<n;a++)
            {
            xold[a]=x[a];
            }

        }
    }


}

int main(){
	int n = 0;
	cout<<"Size\n";
	cin>>n;
	sor(n);
	return 0;
}