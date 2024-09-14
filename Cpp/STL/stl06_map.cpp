// Map
/*
    Maps: Key value pairs
        : Value stored in sorted order of keys
        : Red Black Trees data structure use to implement maps.
        : Map keys unique, duplicate keys are not allow.
        : insertion and accessing the value time complexity is O(log(n))
    Unordered Maps: 
    Multimaps(basic introduction)
*/
#include <bits/stdc++.h>

using namespace std;

#define DEBUG 3

template <class A, class B>
void print(const std::map<A, B> &m);

int main(int argc, char *argv[]) {
    #if defined(DEBUG) && DEBUG ==  1
        try {
            map<int, string> m;
            m[1] = "abc";   // O(log(n))
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

            std::cout << "Method04 : Print Map" << std::endl;
            print(m);


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

            print(m);

            // map methods. if no value the return m.end()
            auto val = m.find("Arjun");
            std::cout << val->first << " : " << val->second << std::endl;

            val = m.find("Anuj");
            if(val != m.end()){
                std::cout << val->first << " : " << val->second << std::endl;
            } else {
                std::cout << "No key exist." << std::endl;
            } 

            std::cout << "Program Ends" << std::endl;

        } catch(const std::exception &e) {
            std::cout << "Main Error 02 : " << e.what() << std::endl;
        }

    
    #elif defined(DEBUG) && DEBUG == 3
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

            print(m);

            // delete some values
            m.erase("Sudhanshu");  // O(log(n))  n = size of map
            print(m);

            m.erase("Akash");
            print(m);

            auto it = m.find("Nilesh");
            m.erase(it);
            print(m);

            it = m.find("Suresh");
            if (it != m.end()) {
                m.erase(it);
                print(m);
            } else {
                std::cout << "Key not Exist" << std::endl;
            }

            m.clear();
            print(m);

            std::cout << "Program Ends" << std::endl;
            

        } catch (const exception &e) {
            std::cout << e.what() << std::endl;
        }

    
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
