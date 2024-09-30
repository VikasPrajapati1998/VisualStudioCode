#include <bits/stdc++.h>

using namespace std;

#define DEBUG 1

template<class A> 
void print(A temp);

int main(int argc, char *argv[]) {
    #if defined(DEBUG) && DEBUG == 1
    {
        // multiset
        int t;
        std::cin >> t;
        while(t--) {
            int n, k;
            std::cin >> n >> k;
            multiset<long long> bags;
            for(int i=0; i<n; ++i) {
                int candy_ct;
                std::cin >> candy_ct;
                bags.insert(candy_ct);
            } 
            long long total_candies = 0;
            for (int i=0; i<k; i++) {
                auto last_it = (--bags.end());
                int candy_ct = *last_it;
                total_candies += candy_ct;
                bags.erase(last_it);
                bags.insert(candy_ct / 2);
            }
        }
    }

    #endif

    return 0;
    
}

template<class A>
void print(A temp) {
    for (auto &iter: temp)
        std::cout << iter << ", ";
    
}


