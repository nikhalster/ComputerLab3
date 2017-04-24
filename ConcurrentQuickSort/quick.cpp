#include <iostream>
#include <omp.h>

using namespace std;


int k = 0;


int partition(int A[],int p,int r){
  int i = p;
  
  for (int j = p; j < r-1; j++)
  {
    if (A[j] <= A[r-1])
    {
      swap(A[i],A[j]);      
      ++i;
    }
  }

  swap(A[i],A[r-1]);
  return i;
}

void swap(int &a, int &b){
      int temp = a;
      a = b;
      b = temp;
}

void quick_sort(int a[],int p,int r)
{
   int j;
   if(p<r)
    {
      j = partition(a,p,r);
      cout<<"Pivot element "<<a[j]<<"has been found out by thread "<<k<<"\n\n";

      #pragma omp parallel sections // just recursively do the same things for the sub arrays 
      {
        #pragma omp section
        {
          k++;
          quick_sort(a,p,j);
        }

        #pragma omp section
        {
          k++;
          quick_sort(a,j+1,r);
        }
      }
    }
}



int main()
{
  int n,i;
  cout<<"\nEnter the number of elements in the array that you want to sort: ";
  cin>>n;
  int a[n];
  cout<<"\nEnter all "<<n<<" numbers : ";
  for(i=0;i<n;i++)
    cin>>a[i];

  quick_sort(a,0,n);

  cout<<"\n\nAfter sorting using quick sort we get : \n";
  for(i=0;i<n;i++)
    cout<<a[i]<<"\t";

    cout<<"\n";
    return 0;
}