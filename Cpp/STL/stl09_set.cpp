// Set and multiset
// Collection of elements, just like the keys of map.
// Store elements in sorted ordered and store unique elements.

#include <bits/stdc++.h>

using namespace std;

// macros
#define DEBUG 4

// function declaration
void print(set<string> &s);
void display(set<string> &s);

// main
int main(int args, char *argv[]) {
    #if defined(DEBUG) && DEBUG == 1
    {
        // set: orderd, unique, log(n)
        set<string> s;
        s.insert("Beta"); // log(n)
        s.insert("Gama");
        s.insert("Alpha");
        s.insert("Delta");
        s.insert("Charli");
        s.insert("Bravo");
        print(s);

        // iterator
        set<string> ::iterator itr = s.begin();
        std::cout << *itr << std::endl;

        // find
        auto it = s.find("Delta");
        if (it != s.end()) {
            std::cout << "Find: " << (*it);
        }
        std::cout << std::endl;

        // erase by iterator
        s.erase(it);
        display(s);

        // erase by value
        s.erase("Bravo");
        display(s);

    }

    #elif defined(DEBUG) && DEBUG == 2
    {
        std::cout << "Set : " << std::endl;
        set<string> s;
        int n=0;
        std::cout << "Enter n: ";
        std::cin >> n;
        int i=0;
        for (i=0; i<n; ++i) {
            string str;
            std::cout << "Enter " << i+1 <<" value: " ;
            std::cin >> str;
            s.insert(str);
        }

        for(auto value: s) {
            std::cout << value << ", ";
        }
        std::cout << std::endl;

    }

    #elif defined(DEBUG) && DEBUG == 3
    {
        std::cout << "Unordered Set : " << std::endl;
        // unordered_set: Use hastable, unordered, unique, O(n)
        unordered_set<string> us;
        int n=0;
        std::cout << "Enter n: ";
        std::cin >> n;
        
        int i=0;
        for (i=0; i<n; ++i) {
            string str;
            std::cout << "Enter Value: ";
            std::cin >> str;
            us.insert(str);
        }
        
        for (auto value: us) {
            std::cout << value << ", "; 
        }
        std::cout << std::endl;

        string find_value;
        std::cout << "Enter find value: "; std::cin >> find_value;
        auto it = us.find(find_value);
        if (it != us.end()) { std::cout << *it << std::endl; } else { std::cout << "Value not present."; }
    }

    #elif defined(DEBUG) && DEBUG == 4
    {
        std::cout << "Multiset : " << std::endl;
        // multiset: not-unique, ordered
        multiset<string> ms;
        int n=0;
        std::cout << "Enter n:"; std::cin >> n;
        
        int i=0;
        for (i=0; i<n; ++i) {
            string str;
            std::cout << "Enter value: "; std::cin >> str;
            ms.insert(str);
        }

        for (auto &value: ms) {
            std::cout << value << ", ";
        }
        std::cout << std::endl;

        // find retur first value
        string find_value;
        std::cout << "Enter find value: "; std::cin >> find_value;
        auto it = ms.find(find_value);
        if(it != ms.end()) { std::cout << *it << std::endl; } else { std::cout << "None" << std::endl; }

        for (auto &value: ms) {
            std::cout << value << ", ";
        }
        std::cout << std::endl;

        // erase the value
        // erase bye the value will erase all the value from the multiset
        string erase_by_value;
        std::cout << "Enter erase by value: "; std::cin >> erase_by_value;
        ms.erase(erase_by_value);

        for (auto &value: ms) {
            std::cout << value << ", ";
        }
        std::cout << std::endl;

        // erase by the iterator
        string erase_by_iter;
        std::cout << "Enter erase by iter: "; std::cin >> erase_by_iter;
        auto itr = ms.find(erase_by_iter);
        if (itr != ms.end()){
            ms.erase(itr);
        }
        
        for (auto &value: ms) {
            std::cout << value << ", ";
        }
        std::cout << std::endl;

    }

    #elif defined(DEBUG) && DEBUG == 5
    {
        std::cout << "Unordered Multiset : " << std::endl;
        // unordered_multiset: unordered, not-unique
        unordered_multiset<string> ums;
        int n=0;
        std::cout << "Enter n: "; std::cin >> n;

        int i=0;
        for (i=0; i<n; i++) {
            string str;
            std::cout << "Enter value: "; std::cin >> str;
            ums.insert(str);
        }

        for (auto &value : ums) {
            std::cout << value << ", ";
        }
        std::cout << std::endl;

    }

    #endif
}


// function definition
// =============================================================================
void print(set<string> &s) {
    for (auto value : s) {
        std::cout << value << ", ";
    }
    std::cout << std::endl;

    // for (auto it=s.begin(); it != s.end(); ++it) {
    //     std::cout << *it << ", ";
    // }
    // std::cout << std::endl;
}
// =============================================================================

void display(set<string> &s) {
    for (string value : s) {
        std::cout << value << ", ";
    }
    std::cout << std::endl;
}
