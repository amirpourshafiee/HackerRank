/*
Chief's bot is playing an old DOS-based game. There are  buildings in the game - indexed from  to  and are placed left-to-right. It is guaranteed that building with index  will be of height  unit. For buildings with index  () height will be  units.

At beginning Chief's bot is at building with index . At each step, bot jumps to next (right) building. Suppose bot is at  building and his current energy is , then in next step he will jump to  building. He will gain/lose energy equal in amount to difference between  and

If , then he will lose  units of energy.
Otherwise, he will gain  units of energy.
Goal is to reach  building, and during the course bot should never have negative energy units. What should be the minimum units of energy with which bot should start to successfully complete the game?

Input Format

The first line contains integer . Next line contains  space separated integers  representing the heights of the buildings.

Output Format

Print a single integer representing minimum units of energy required to complete the game.

Constraints


Sample Input

5
3 4 3 2 4
sample Output

4
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N,hi;
    cin>>N;
    vector<int> h;
    for(int i=0;i<N;i++)
        {
        cin>>hi;
        h.push_back(hi);
    }
    int e=0;
    for(int i=N-1;i>=0;i--)
        {
        e = (e+h[i]+1)/2;
    }
    cout<<e;
    return 0;
}
