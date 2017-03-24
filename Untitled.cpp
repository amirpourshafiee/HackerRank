
void pascalTriangle(int k) {
for (int i= 0; i<k; i++){
    int num =1;
    for (int j=1; j<=i; j++)
    {
        cout<<num;
        num = num* (i-j)/(j+1);
    }  
  }
}
