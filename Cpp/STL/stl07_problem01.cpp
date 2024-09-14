/*
Given N strings, print unique strings in lexiographical order with their frequency.
N <= 10^5
|S| <= 100
*/

#include <bits/stdc++.h>
using namespace std;

# define DEBUG 1

template <class A, class B>
void print(const std::map<A, B> &m);

int main(int argc, char *argv[]) {
#if defined(DEBUG) && DEBUG == 1
    map<string, int> m;
    int n = 0;
    std::cin >> n;

    for (int i=0; i<n; ++i) {
        string s;
        std::cin >> s;
        // m[s] = m[s] + 1;
        m[s]++;
    }
    
    print(m);


#endif
}


template <class A, class B>
void print(const std::map<A, B> &m) {
    std::cout << "Size of Map : " << m.size() << std::endl;
    for (auto &mp : m) {
        std::cout << mp.first << " : " << mp.second << std::endl;
    }
    std::cout << std::endl;
}
