#include <bits/stdc++.h>
// #include <typeinfo>

using namespace std;

#define DEBUG 8

template<class T> void printVec(vector<T> &vec);
template <class A, class B> void printPairVec(vector<pair<A, B>> &vec); 

// ===============================================================================================
int main(int argc, char *argv[]) {
    try {
        // vector of pairs
        #if defined(DEBUG) && DEBUG == 1  // vector of pair  =====================================
        vector<pair<int, string>> v = { {1, "Arjun Prajapati"}, 
                                        {2, "Vikas Prajapati"}, 
                                        {3, "Sudhanshu Mishra"}, 
                                        {4, "Shailedra Prajapati"}, 
                                        {5, "Anupam Dixit"},
                                        {6, "Ayush Vishwakarma"},
                                        {7, "Divyanshu Shukla"}
                                    };
        printPairVec(v);

        vector<pair<int, int>> v1{{1, 10}, {2, 20}, {3, 30}, {4, 40}, {5, 50}, {6, 60}};
        printPairVec(v1);

        #elif defined(DEBUG) && DEBUG == 2  // vector of pair ====================================
        vector<pair<int, int>> v1 = { {1, 100}, {2, 99}, {3, 98}, {4, 97}, {5, 96}, {6, 95}, {7, 94}, {8, 93}, {9, 92}, {10, 91} };
        printPairVec(v1);

        #elif defined(DEBUG) && DEBUG == 3  // type id ===========================================
        vector<pair<int, float>> v2;
        std::cout << typeid(v2).name() << std::endl;
        double num;
        std::cout << typeid(num).name() << std::endl;

        #elif defined(DEBUG) && DEBUG == 4  // vector of pair ====================================
        vector<pair<int, string>> vec;
        int size=0;
        std::cout << "Enter the size of vector : "; std::cin >> size;
        int roll=0;
        string name;
        for (int i=0; i<size; i++) {
            std::cout << "Enter the pair : "; std::cin >> roll >> name;
            // vec.push_back({roll, name});
            vec.push_back(make_pair(roll, name));
            fflush(stdin);
        }

        std::cout << std::endl;
        printPairVec(vec);
        std::cout << std::endl;


        #elif defined(DEBUG) && DEBUG == 5  // array of vectors ==================================
        int vec_arr_size = 0;
        fflush(stdin); std::cout << "Enter the size of array of vectors : "; std::cin >> vec_arr_size;
        vector<int> vec_arr[vec_arr_size]; // N vectors of size n
        int val = 0;
        int vec_size = 0;
        for (int i=0; i<vec_arr_size; i++) {
            fflush(stdin); std::cout << "Enter the size of vector : "; std::cin >> vec_size;
            for (int j=0; j<vec_size; j++) {
                val = (j+1)*(i+1);
                vec_arr[i].push_back(val);
            }
            val = 0;
        }

        std::cout << std::endl;
        for (int i=0; i<vec_arr_size; i++)
            printVec(vec_arr[i]);
        std::cout << std::endl;
        
        
        #elif defined(DEBUG) && DEBUG == 6  // vector of vectors =================================
        // number of cols are dynamic
        int vec_of_vec_size=0;
        fflush(stdin); std::cout << "Enter the size of vector of vector : "; std::cin >> vec_of_vec_size;
        vector<int> vec_of_vec[vec_of_vec_size];  // array of vector
        int val = 0;
        int vec_size = 0;
        for (int i=0; i<vec_of_vec_size; i++) {
            fflush(stdin); std::cout << "Enter the size of vector : "; std::cin >> vec_size;
            for (int j=0; j<vec_size; j++) {
                val = (j+1)*(i+1);
                vec_of_vec[i].push_back(val);
            }
        }

        std::cout << std::endl;
        for (int i=0; i<vec_of_vec_size; i++)
            printVec(vec_of_vec[i]);
        std::cout << std::endl;
        

        #elif defined(DEBUG) && DEBUG == 7  // vector of vectors =================================
        // Number of rows and cols are dynamic
        vector<vector<int>> vec_of_vec;
        int size_N = 0, size_n = 0, var = 0;;
        fflush(stdin); std::cout << "Enter the size_N : "; std::cin >> size_N;
        for (int i=0; i<size_N; i++) {
            // create a temp vector
            fflush(stdin); std::cout << "Enter the size_n : "; std::cin >> size_n;
            vector<int> temp;
            for (int j=0; j<size_n; j++) {
                fflush(stdin); std::cout << "Enter the value : "; std::cin >> var;
                temp.push_back(var);
                var = 0;
            }
            vec_of_vec.push_back(temp);
        }
        vec_of_vec[0].push_back(10); // push a number of first vector of vector
        vec_of_vec.push_back(vector<int> ()); // push a empty vector
        vec_of_vec.push_back(vector<int> (11, 22, 33));  // push a vector in vector

        // print the vector
        std::cout << std::endl;
        for (int i=0; i<vec_of_vec.size(); i++)
            printVec(vec_of_vec[i]);
        std::cout << std::endl;
        

        #elif defined(DEBUG) && DEBUG == 8  // vector of vectors =================================
        // Number of rows and cols are dynamic
        vector<vector<int>> vec_of_vec;
        int size_N{0}, size_n{0}, var{0};
        fflush(stdin); std::cout << "Enter the size_N : "; std::cin >> size_N;
        for (int i=0; i<size_N; i++) {
            fflush(stdin); std::cout << "Enter the size_n : "; std::cin >> size_n;
            vec_of_vec.push_back(vector<int> ()); // push the empty vector
            for (int j=0; j<size_n; j++) {
                fflush(stdin); std::cout << "Enter the value : "; std::cin >> var;
                vec_of_vec[i].push_back(var);
                var = 0;
            }
        }

        // print vector
        std::cout << std::endl;
        for (int i=0; i<vec_of_vec.size(); i++)
            printVec(vec_of_vec[i]);
        std::cout << std::endl;
        

        #else   // ===============================================================================
        std::cout << "No Vector of Pairs." << std::endl;

        #endif  // ===============================================================================

    } catch (exception &e) {
        std::cout << "Main Function Error : " << e.what() << std::endl;
    }
}
// ===============================================================================================


template<class T> void printVec(vector<T> &vec) {
    std::cout << "[";
    for (int i=0; i<vec.size(); i++) {
        std::cout << vec[i];
        if (i != vec.size() - 1)
            std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}


template <class A, class B> void printPairVec(vector<pair<A, B>> &vec) {
    for (int i=0; i<vec.size(); i++)
        std::cout << "(" << vec[i].first << ", " << vec[i].second << ")" << std::endl;
    std::cout << std::endl;
}

