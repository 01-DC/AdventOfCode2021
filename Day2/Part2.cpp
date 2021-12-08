#include <bits/stdc++.h>
#define ll long long int
#define rep(i, A, B) for(int i= A; i < B; i++)
#define FastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

int main()
{
    FastIO
    ifstream inp;
    string direction; int units;
    inp.open("input.txt");
    // inp.open("test.txt");
    int X= 0, Y= 0, aim= 0;
    while(inp >> direction >> units)
    {
        switch(direction[0])
        {
            case 'f':
                X+= units;
                Y+= units*aim;
                break;
            case 'u':
                aim-= units;
                break;
            case 'd':
                aim+= units;
        }
    }
    cout << X*Y << endl;
    return 0;
}
