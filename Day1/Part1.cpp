#include <bits/stdc++.h>
#define ll long long int
#define rep(i, A, B) for(int i= A; i < B; i++)
#define FastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

int main()
{
    FastIO
    ifstream inp;
    int prev= INT_MAX, num, ans= 0;
    inp.open("input.txt");
    while(inp >> num)
    {
        if(num>prev)
            ans++;
        prev= num;
    }
    cout << ans << endl;
    return 0;
}
