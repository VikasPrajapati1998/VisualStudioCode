/*
# Unorderd map
1. inbuilt implementation : map use Red-Black trees, Unordered_map use hash table
2. Time Complexity : O(1)
3. Valid keys datatypes : pair, set and many are not allow as key in unorderd_map
4. Key duplication not allow

# multimap
1. many keys with same name are allow in the multimap.
2. Key duplication allow.
*/

#include <bits/stdc++.h>
using namespace std;

#define DEBUG 3

template <class A, class B>
void print(const std::unordered_map<A, B> &m);

int main(int argc, char *argv[]) {
    #if defined(DEBUG) && DEBUG == 1 
    {
        unordered_map<int, string> m;
        m[1] = "Vipul";
        m[4] = "Praful";
        m[7] = "Satyam";
        m[3] = "Arjun";
        m[5] = "Akash";
        m[2] = "Prashant";
        m[6] = "Amit";

        print(m);

        auto it = m.find(3);
        if(it != m.end()){
            std::cout << it->first << " : " << it->second << std::endl;
        } else {
            std::cout << "No key exist." << std::endl;
        }

        it = m.find(9);
        if(it != m.end()){
            std::cout << it->first << " : " << it->second << std::endl;
        } else {
            std::cout << "No key exist." << std::endl;
        }
    }


    #elif defined(DEBUG) && DEBUG ==  2
    {
        unordered_map<string, int> m;
        int n = 0;
        std::cin >> n;

        for (int i=0; i<n; ++i) {
            string s;
            std::cin >> s;
            // m[s] = m[s] + 1;
            m[s]++;
        }
        
        print(m);

        int q;
        cin >> q;
        while(q--) {
            string s;
            std::cin >> s;
            std::cout << m[s] << std::endl;
        }
    }

    #elif defined(DEBUG) && DEBUG == 3
    {
        multimap<int, string> m;
        m.insert({1, "Vipul"});
        m.insert({4, "Praful"});
        m.insert({2, "Satyam"});
        m.insert({3, "Arjun"});
        m.insert({1, "Akash"});
        m.insert({2, "Prashant"});
        m.insert({3, "Amit"});

        std::cout << "Size of the multimap : " << m.size() << std::endl;
        for (auto &it : m) {
            std::cout << it.first << " : " << it.second << std::endl;
        }
        std::cout << std::endl;


    }
    #endif
}


template <class A, class B>
void print(const std::unordered_map<A, B> &m) {
    std::cout << "Size of Map : " << m.size() << std::endl;
    for (auto &mp : m) {
        std::cout << mp.first << " : " << mp.second << std::endl;
    }
    std::cout << std::endl;
}
