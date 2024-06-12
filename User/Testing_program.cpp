#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n'
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM =
            chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }

    size_t operator()(const std::string &str) const {
        static const uint64_t FIXED_RANDOM =
            chrono::steady_clock::now().time_since_epoch().count();
        uint64_t hash = FIXED_RANDOM;
        for(char c : str) {
            hash ^= (hash << 5) + (hash >> 2) + c;
        }
        return splitmix64(hash);
    }
};
signed main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int n, maxi = 0;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) {
        cin >> a[i];
        maxi = max(maxi, a[i]);
    }
    vector<int> sieve(maxi + 1, 1);
    sieve[0] = 0, sieve[1] = 0;
    for(int i = 2; i * i <= maxi; i++) {
        if(sieve[i])
            for(int j = i * i; j <= maxi; j += i) sieve[j] = 0;
    }
    unordered_map<int, int, custom_hash> prms;
    for(int i = 0; i < n; i++) {
        for(int j = 1; j * j <= a[i]; j++) {
            if(a[i] % j == 0) {
                if(sieve[j]) prms[j]++;
                if(a[i] / j != j and sieve[a[i] / j]) prms[a[i] / j]++;
            }
        }
    }
    int ans = 1;
    for(auto &[p, c] : prms) 
        ans = max(ans, c);
    cout << ans;
    return 0;
}