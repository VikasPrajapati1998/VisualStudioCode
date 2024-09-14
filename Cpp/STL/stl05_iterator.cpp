// Iterator : Use to access the value of containers.

#include <bits/stdc++.h>

using namespace std;

# define DEBUG 5

// function decleration
template<class T> void printVec(vector<T> &vec);

// =============================================================================================================
int main(int argc, char *argv[]) {
    #if defined(DEBUG) && DEBUG == 1
        vector<int> vec = {2, 3, 5, 6, 7};
        for(int i=0; i< vec.size(); ++i){
            std::cout << vec[i] << ", ";
        }
        std::cout << std::endl;

        printVec(vec);

        // declear a iterator
        vector<int> ::iterator it = vec.begin();
        std::cout << (*it) << std::endl;
        std::cout << *(it+1) << std::endl;

        vector<int> ::iterator itr = vec.begin();
        for(itr=vec.begin(); itr != vec.end(); ++itr){
            std::cout << *itr << ", ";
        }
        std::cout << std::endl;
        /*
        itr++ : next iterator (prefer to use)
        itr+1 : next location
        */

   #elif defined(DEBUG) && DEBUG == 2
        // make pairs
        pair<int, string> p = {1, "Vikas"};
        std::cout << p.first << ", " << p.second << std::endl;
        std::cout << std::endl;

        // array of pairs
        pair<int, string> array_of_pairs[5] = {{1, "Arjun"}, {2, "Sudhanshu"}, {3, "Shivani"}, {4, "Jiya"}, {5, "Jyoti"}};
        for(int i=0; i<5; i++){
            std::cout << "{" << array_of_pairs[i].first << ", " << array_of_pairs[i].second << "}" << std::endl;
        }
        std::cout << std::endl;

        // vector of pairs
        vector<pair<int, string>> vector_of_pair = {{1, "Arjun"}, {2, "Jiya"}, {3, "Vikas"}, {4, "Jyoti"}, {5, "Shivi"}};
        vector<pair<int, string>> ::iterator it;
        for(it = vector_of_pair.begin(); it != vector_of_pair.end(); ++it){
            std::cout << (*it).first << " : " << (*it).second << std::endl;
        }
        std::cout << std::endl;

        // method 2 : print the using iterator
        for(it = vector_of_pair.begin(); it != vector_of_pair.end(); ++it){
            std::cout << it->first << " : " << it->second << std::endl;
        }
        std::cout << std::endl;


    #elif defined(DEBUG) && DEBUG == 3
        // must have cpp-11 or above version
        // range based loop, auto keywords
        // vector of pairs
        vector<int> vec = {2, 3, 5, 6, 7};
        for(int value : vec){
            std::cout << value << ", ";
        }
        std::cout << std::endl << std::endl;

        vector<pair<int, string>> vector_of_pair = {{1, "Arjun"}, {2, "Jiya"}, {3, "Vikas"}, {4, "Jyoti"}, {5, "Shivi"}};
        vector<pair<int, string>> ::iterator it;  // iterator
        for(pair<int, string> value: vector_of_pair){
            std::cout << "{" << value.first << ", " << value.second << "}" << std::endl;
        }
        std::cout << std::endl;

        // auto keywards
        auto a = 1;
        auto b = 1.2;
        std::cout << a << ", " << b << std::endl;

    
    #elif defined(DEBUG) && DEBUG == 4
        // must have cpp-11 or above version
        // range based loop, auto keywords
        vector<int> vec = {2, 4, 6, 8, 10};
        // vector<int> ::iterator it;

        // Method 01: Print the container
        for(auto it = vec.begin(); it != vec.end(); ++it){
            std::cout << *it << ", ";
        }
        std::cout << std::endl;

        // Method 02: Print the container
        for (auto it : vec){
            std::cout << it << ", ";
        }
        std::cout << std::endl;

        // vector of pairs 
        vector<pair<int, string>> vector_of_pair = {
            {1, "Arjun"},
            {2, "Brijesh"},
            {3, "Chittra"},
            {4, "Dinesh"},
            {5, "Eskiamal"},
            {6, "Fatima"}
        };
        for(auto it: vector_of_pair){
            std::cout << it.first << " : " << it.second << ", ";
        }
        std::cout << std::endl;

        for(auto &it: vector_of_pair){
            std::cout << it.first << " : " << it.second << ", ";
        }
        std::cout << std::endl;

    #elif defined(DEBUG) && DEBUG == 5
        vector<int> key = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        vector<string> value = {"Aman", "Pawan", "Amit", "Ankush", "Akshay", "Dinesh", "Krishna", "Suresh", "Mahesh", "Vishnu"};
        vector<pair<int, string>> vector_of_pairs = {};

        // Insert the value in the vector_of_pairs
        std::cout << "Start Putting Value" << std::endl;
        for(int i_key=0, j_value=0;  (i_key<key.size()) && (j_value<value.size()); ++i_key, ++j_value){
            vector_of_pairs.push_back(make_pair(key[i_key], value[j_value]));
        }

        // Print the vector_of_pairs Method 01
        std::cout << "Method01 : Print the Vector of Pairs" << std::endl;
        for(auto it = vector_of_pairs.begin(); it != vector_of_pairs.end(); ++it){
            std::cout << it->first << " : " << it->second << std::endl;
        }
        std::cout << std::endl;

        // Print the vector_of_pairs Method 02
        std::cout << "Method02 : Print the Vector of Pairs" << std::endl;
        for(auto &it: vector_of_pairs){
            std::cout << it.first << " : " << it.second << std::endl;
        }
        std::cout << std::endl;



    #endif
}
// =============================================================================================================


template<class T> void printVec(vector<T> &vec) {
    std::cout << "[";
    for (int i=0; i<vec.size(); i++) {
        std::cout << vec[i];
        if (i != vec.size() - 1)
            std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}
