#include <bits/stdc++.h>
#define ll long long int
#define rep(i, A, B) for(int i= A; i < B; i++)
#define FastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

int main()
{
    FastIO
    ifstream inp;
    // inp.open("test.txt");
    inp.open("input.txt");
    string line;
    // stringstream gamma, epsilon;
    int gamma= 0, epsilon= 0;
    map<int, int> counts;
    int total= 0;
    while(inp >> line)
    {
        total++;
        rep(i, 0, line.length())
            counts[i]+= line[i] - 48;
    }
    total/= 2; int power= line.length()-1;
    rep(i, 0, line.length())
    {
        if(counts[i]>=total)
            gamma+= 1<<power;
        else
            epsilon+= 1<<power;
        power--;
    }
    // int Gamma= 0, Epsilon= 0, power= N-1; char ch;
    // while(gamma >> ch)
    // {
    //     if(ch=='1')
    //         Gamma+= 1<<power;
    //     power--;
    // }
    // power= N-1;
    //  while(epsilon >> ch)
    // {
    //     if(ch=='1')
    //         Epsilon+= 1<<power;
    //     power--;
    // }
    cout << gamma*epsilon << endl;
}