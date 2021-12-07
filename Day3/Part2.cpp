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
    vector<string> O2;
    vector<string> CO2;

    while(inp >> line)
    {
        O2.push_back(line);
        CO2.push_back(line);
    }

    int N= line.length();
    //for oxygen generator rating
    //We count 1 and remove all 0's at i if 1 is more common else remove 1
    int count_one, total_size;
    rep(i, 0, N)
    {
        count_one= 0; total_size= (O2.size()%2==0)? (O2.size()/2 - 1) : (O2.size()/2);
        for(auto &it : O2)
            count_one+= (it[i]=='1')? 1 : 0;

        if(count_one>total_size)
        {
            for(auto it=O2.begin(); it!=O2.end() && O2.size()>1; ++it)
                if((*it)[i]=='0')
                    O2.erase(it--);
        }
        else
        {
            for(auto it=O2.begin(); it!=O2.end() && O2.size()>1; ++it)
                if((*it)[i]=='1')
                    O2.erase(it--);
        }
    }

    //for carbon dioxide scrubber rating
    //We count 1 and remove 1's at position i if 1 is the more common else remove 0
    rep(i, 0, N)
    {
        count_one= 0; total_size= (CO2.size()%2==0)? (CO2.size()/2 - 1) : (CO2.size()/2);
        for(auto &it : CO2)
            count_one+= (it[i]=='1')? 1 : 0;

        if(count_one>total_size)
        {   
            for(auto it=CO2.begin(); it!=CO2.end() && CO2.size()>1; ++it)
                if((*it)[i]=='1')
                    CO2.erase(it--);
        }
        else
        {   
            for(auto it=CO2.begin(); it!=CO2.end() && CO2.size()>1; ++it)
                if((*it)[i]=='0')
                    CO2.erase(it--);
        }
    }

    int O2_rating= 0, CO2_rating= 0;
    for(int power= N; power>0; --power)
    {
        O2_rating+= (O2[0][N-power]-48)<<(power-1);
        CO2_rating+= (CO2[0][N-power]-48)<<(power-1);
    }
    
    cout << O2_rating*CO2_rating << endl;
}