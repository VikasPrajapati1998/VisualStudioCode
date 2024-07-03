// Advance in vector
#include <bits/stdc++.h>

#define DEBUG 1

using namespace std;

template<class T> void printVec(vector<T> &vec);

int main(int argc, char *argv[]) {
    try {
        #if defined(DEBUG) && DEBUG == 1
        vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        printVec(v);

        vector<int> v1{2, 3, 4, 5, 6};
        printVec(v1);

        vector<string> v2{"Arjun Prajapati", "Sudhanshu Mishra", "Shailendra Prajapati", "Anupam Dixit", "Anil Jalwanshi"};
        printVec(v2);

        vector<float> v3;
        for(float i=0.0; i<10.0; i=i+0.5)
            v3.push_back(i);
        printVec(v3);

        vector<long> v4;
        int var=0;
        for(int i=1; i<=10; i++) {
            var = i * 10;
            v4.push_back(var);
        }
        printVec(v4);

        #endif

        return 0;
    } catch (exception &e) {
        std::cout << e.what() << std::endl;
    }
}

/*
template<class T> void printVec(vector<T> &vec) {
    std::cout << "[";
    for (int i=0; i<vec.size(); i++) {
        std::cout << vec[i];
        if (i != vec.size() - 1)
            std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}
*/

template<class T> void printVec(vector<T> &vec) {
    std::cout << "[ ";
    for (T v : vec) 
        std::cout << v << ", ";
    std::cout << "]" << std::endl;
}
