// Map
/*
    Maps: Key value pairs
        : Value stored in sorted order of keys
        : Red Black Trees data structure use to implement maps.
    Unordered Maps: 
    Multimaps(basic introduction)
*/
#include <bits/stdc++.h>

using namespace std;

#define DEBUG 2

int main(int argc, char *argv[]) {
    #if defined(DEBUG) && DEBUG ==  1
        try {
            map<int, string> m;
            m[1] = "abc";
            m[5] = "cdc";
            m[3] = "acd";

            m.insert({4, "afg"});
            m.insert({2, "pqr"});

            std::cout << "Method01 : Print Map" << std::endl;
            map<int, string> ::iterator it;
            for (it = m.begin(); it != m.end(); ++it) {
                std::cout << it->first << " : " << it->second << std::endl;
            }
            std::cout << std::endl;

            std::cout << "Method02 : Print Map" << std::endl;
            for (auto it = m.begin(); it != m.end(); ++it) {
                std::cout << it->first << " : " << it->second << std::endl;
            }
            std::cout << std::endl;

            std::cout << "Method03 : Print Map" << std::endl;
            for (auto &it: m) {
                std::cout << it.first << " : " << it.second << std::endl;
            }
            std::cout << std::endl;


        }catch(exception &e){
            std::cout << "Main Error 01 : " << e.what() << std::endl;
        }

    #elif defined(DEBUG) && DEBUG == 2
        try {
            map<string, int> m;
            m["Sudhanshu"] = 1;
            m["Brijesh"] = 2;
            m["Pawan"] = 3;
            m["Arjun"] = 4;
            m["Shailendra"] = 5;
            m["Praful"] = 6;
            m["Akash"] = 7;

            m.insert(make_pair("Nilesh", 8));
            m.insert({"Chandan", 9});
            m.insert({"Dinesh", 10});

            // Print the map
            for (auto &it : m) {
                std::cout << it.first << " : " << it.second << std::endl;
            }
            std::cout << std::endl;

        } catch(exception &e) {
            std::cout << "Main Error 02 : " << e.what() << std::endl;
        }

    
    #endif
}

