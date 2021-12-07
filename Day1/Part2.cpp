#include <bits/stdc++.h>
#define ll long long int
#define rep(i, A, B) for(int i= A; i < B; i++)
#define FastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

int main()
{
    FastIO
    ifstream inp;
    inp.open("input.txt");

    int prev1, prev2, curr;
    inp >> prev2;
    // istringstream(line) >> prev2;
    inp >> prev1;
    // istringstream(line) >> prev1;
    
    int ans= 0, prev_sum= INT_MAX, curr_sum;

    while(inp >> curr)
    {
        // cout << curr << endl;
        curr_sum= prev1 + prev2 + curr;
        if(curr_sum > prev_sum)
            ans++;

        prev_sum = curr_sum;
        prev2= prev1;
        prev1= curr;
    }
    cout << ans << endl;
    return 0;
}
