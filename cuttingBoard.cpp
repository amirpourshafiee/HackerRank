/*
Alice gives Bob a board composed of  wooden squares and asks him to find the minimum cost of breaking the board back down into individual  pieces. To break the board down, Bob must make cuts along its horizontal and vertical lines.

To reduce the board to squares,  vertical cuts must be made at locations  and horizontal cuts must be made at locations . Each cut along some  (or ) has a cost,  (or ). If a cut of cost  passes through  already-cut segments, the total cost of the cut is .

The cost of cutting the whole board down into  squares is the sum of the cost of each successive cut. Recall that the cost of a cut is multiplied by the number of already-cut segments it crosses through, so each cut is increasingly expensive.

Can you help Bob find the minimum cost?

Input Format

The first line contains a single integer, , denoting the number of queries. The  subsequent lines describe each query over  lines according to the following format:

The first line has two positive space-separated integers,  and , detailing the respective height () and width () of the board.
The second line has  space-separated integers listing the cost, , of cutting a segment of the board at each respective location from .
The third line has  space-separated integers listing the cost, , of cutting a segment of the board at each respective location from .
Note: If we were to superimpose the  board on a 2D graph, , , , and  would all be edges of the board and thus not valid cut lines.

Constraints

Output Format

For each of the  queries, find the minimum cost () of cutting the board into  squares and print the value of .

Sample Input:
1
2 2
2
1

Sample Output:
4
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
bool cmp(pair<long long int,char> a, pair<long long int ,char> b)
    {
    return a.first>b.first;
}
int main() {
   long long int i,j,k,v,t,n,m;
    cin>>t;
    for(v=0;v<t;v++)
        {
        cin>>m>>n;
        vector<pair<long long int,char>>vect;
        for(i=0;i<m-1;i++)
            {
            cin>>j;
            vect.push_back(make_pair(j,'h'));
        }
         for(i=0;i<n-1;i++)
            {
            cin>>j;
            vect.push_back(make_pair(j,'v'));
        }
        sort(vect.begin(),vect.end(),cmp);
        long long int ht_segments=0,vt_segments=0,ans=0;
        vector<pair<long long int,char>>::iterator ii;
        for(ii=vect.begin();ii!=vect.end();ii++)
            {
            if(ii->second=='h')
                {
                if(ht_segments==0)
                    ht_segments+=2;
                else
                    ht_segments++;
                if(vt_segments>0)
                    ans+=(ii->first*vt_segments);
                else
                    ans+=ii->first;

            }
            else{
                 if(vt_segments==0)
                    vt_segments+=2;
                else
                    vt_segments++;
                if(ht_segments>0)
                    ans+=(ii->first*ht_segments);
                else
                    ans+=ii->first;

            }
        }
        cout<<ans%(1000000007)<<"\n";

    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}
