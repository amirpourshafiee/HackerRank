/*
How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer.

Task

Write a program that, given

The amount  to make change for and the number of types  of infinitely available coins
A list of  coins -
Prints out how many different ways you can make change from the coins to STDOUT.

The problem can be formally stated:

Given a value , if we want to make change for  cents, and we have infinite supply of each of  valued coins, how many ways can we make the change? The order of coins doesn’t matter.

Solving the overlapping subproblems using dynamic programming

You can solve this problem recursively, but not all the tests will pass unless you optimise your solution to eliminate the overlapping subproblems using a dynamic programming solution

Or more specifically;

If you can think of a way to store the checked solutions, then this store can be used to avoid checking the same solution again and again.
Input Format

First line will contain 2 integer N and M respectively.
Second line contain M integer that represent list of distinct coins that are available in infinite amount.

Constraints

The list of coins will contain distinct integers.
Output Format

One integer which is the number of ways in which we can get a sum of N from the given infinite supply of M types of coins.

Sample Input

4 3
1 2 3
Sample Output

4

*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
   long long int c,n,dp[1001][1000]={0},i,j,var;
    cin>>c>>n;
    for(j=0;j<=c;j++){
       dp[0][j+1]=j;
    }
    dp[1][0]=0;
    dp[1][1]=1;
    for(i=2;i<=n+1;i++){
        cin>>var;
        dp[i][0]=var;
    }

    for(i=2;i<=n+1;i++){
        for(j=1;j<=c+1;j++){
          if(dp[i][0]>dp[0][j]) {
              dp[i][j]=dp[i-1][j];
          }else {
     long long       int  var1=dp[i-1][j];
              long long int var2=abs(dp[i][0]-dp[0][j]);
              var2=dp[i][var2+1];
              var1=var1+var2;
              dp[i][j]=var1;
          }
        }
    }
    cout<<dp[n+1][c+1];

    return 0;
}
