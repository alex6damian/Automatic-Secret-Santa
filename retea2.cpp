#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <cmath>
#include <tuple>
#include <iomanip>

using namespace std;
typedef long long ll;
typedef double lf;
ll n, m;
lf euclid(ll x1, ll y1, ll x2, ll y2)
{
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}
int main()
{
    ifstream in("retea2.in");
    ofstream out("retea2.out");

    in >> n >> m;
    vector<vector<pair<ll,ll>>> stations(n+m);
    vector<ll> initStations(n);
    vector<pair<ll, ll>> g(n+m);

    for(ll i = 0; i < n; i++)
    {
        initStations[i] = i;
    }

    for(ll i=0;i< n+m; i++)
    {
        ll x, y;
        in >> x >> y;
        g[i]={x, y};
    }

    for(ll i=0;i< n+m; i++)
    {
        for(ll j=i+1;j<n+m;j++)
        {
            stations[i].emplace_back(j, euclid(g[i].first, g[i].second, g[j].first, g[j].second));
        }
    }

    vector<bool> inMST(n+m, false);
    priority_queue<tuple<lf, ll, ll>, vector<tuple<lf, ll, ll>>, greater<tuple<lf, ll, ll>>> pq;
    lf costF = 0;

    for(auto station : initStations)
    {
        inMST[station] = true;
        for(auto& [neighbor, cost] : stations[station])
        {
            pq.push({cost, station, neighbor});
        }
    }

    while(!pq.empty())
    {
        auto [cost, a, b] = pq.top();
        pq.pop();
        if(inMST[b])
            continue;

        inMST[b] = true;
        costF += cost;

        for(auto& [neighbor, cost] : stations[b])
        {
            if(!inMST[neighbor])
                pq.push({cost, b, neighbor});
        }
    }

    out<<fixed<<setprecision(6)<<costF;
    return 0;
}