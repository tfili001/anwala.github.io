#ifndef JACOBI_H_INCLUDED
#define JACOBI_H_INCLUDED
void jacobi()
{
    ifstream fin("input.txt");
    cout<<"File read\n";
    int n = 3;
    double **A;
    double tol = .001;
    double *b = new double[n];

    double **Temp = createMat(n);
    cout<<"Tmp created\n";
     for(int i=0; i<n; i++)
     {
            for(int j=0; j<n; j++)
            {
                fin>>Temp[i][j];
            }
     }
     cout<<"B Vector\n";

     for(int i=0;i<n;i++)
     {
         fin>>b[i];
         cout<<setprecision(4)<<b[i]<<endl;
     }

     cout<<"Temp read\n";

     ///    uniform_real_distribution<double> dist (-100,100);

     cout<<"______________________\n";
        A = new double *[n];
        for(int i=0; i<n+1; i++)
        {
            A[i]=new double[n+1];
        }
        cout<<"Begin A\n";
           for(int i=0;i<n;i++)
           {
                for(int j=0;j<n+1;j++)
                {
                    if(j==n)
                    {
                        A[i][j]=b[i];
                        cout<<setprecision(4)<<A[i][j]<<"  ";
                    }
                    else
                    {
                        A[i][j]=Temp[i][j];
                        cout<<setprecision(4)<<A[i][j]<<"  ";
                    }
                }
                cout<<endl;
          }

    double *x = new double[n];
    double *xold = new double[n];


	for(int i=0;i<n;i++)
	{
	    double sum = 0.0;
		for(int j=0;j<n;j++)
		{
        cout<<"i="<<i<<" j="<<j<<endl;


            if(j!=i)
            {
                /// CHECK
                cout<<setprecision(4)<<"x["<<i<<"] "<<x[i]<<" 1/A[i][i] "<<1/A[i][i]<<" "<<-A[i][j]<<" "<<xold[j]<<" "<<b[i]<<endl;
                x[i]=(1/A[i][i])*(((-A[i][j])*(xold[j]))+b[i]);
                sum += abs(x[j]-xold[j]);

             //   cout<<fixed<<"tol="<<tol<<" sum="<<sum<<endl;
            }

		}

	}

    for(int i = 0; i < n; i++)
    {
        xold[i] = x[i];
    }
	cout<<"____________________\nX Vector\n";
	for(int i=0;i<n;i++)
	{
		cout<<setprecision(4)<<x[i]<<endl;
	}


}

#endif // JACOBI_H_INCLUDED
