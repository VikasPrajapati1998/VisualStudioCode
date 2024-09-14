#include <bits/stdc++.h>

#define DEBUG 5

using namespace std;

void printVec(vector<int> &vec);
void printVec(vector<string> &vec);

int main(int argc, char *argv[]) {
    try {
        #if defined(DEBUG) && DEBUG == 1
        // vector
        vector<int> v;

        int n; // size of vector
        cout << "Enter the size of vector : "; cin >> n;

        // enter the elements in vector
        for (int i=0; i<n; ++i) {
            int x;
            cout << "Enter value : "; cin >> x;
            v.push_back(x); // O(1)
            printVec(v);
        }

        // pop the value from the vector
        v.pop_back(); // O(1)
        printVec(v);

        // copy the vector
        vector<int> v2 = v; // deep copy  O(n)
        v2.push_back(7);
        printVec(v);
        printVec(v2);

        #elif defined(DEBUG) && DEBUG == 2
        vector<int> v1(7);
        printVec(v1);
        v1.push_back(7);
        printVec(v1);
        v1.push_back(19);
        printVec(v1);

        #elif defined(DEBUG) && DEBUG == 3
        vector<int> v2(10, 3);
        printVec(v2);
        v2.push_back(23);
        printVec(v2);

        #elif defined(DEBUG) && DEBUG == 4
        vector<int> v3;
        int val=0, size=7;
        for(int i=0; i<size; i++) {
            val = (i+1)*3;
            v3.push_back(val);
        }
        printVec(v3);

        #elif defined(DEBUG) && DEBUG == 5
        vector<string> student;
        int size=0;
        cout << "Enter the size : "; cin >> size;

        string name;
        for (int i=0; i<size; i++){
            cout << "Enter name : "; cin >> name;
            student.push_back(name);
        }

        printVec(student);


        #else 
        cout << "No Code will executed." << endl;

        #endif


    } catch(exception &e) {
        cout << "Main Error : " << e.what() << endl;
    }
    return 0;
}


// print the vector
void printVec(vector<int> &vec) {
    try {
        cout << "Size of Vector : " << vec.size() << endl;  // vec.size() O(1) 
        cout << "[";
        for (int i = 0; i < vec.size(); i++) {
            cout << vec[i];
            if (i != vec.size()-1)
                cout << ", ";
        }
        cout << "]" << endl;

    }catch (exception &e) {
        cout << "PrintVec Error : " << e.what() << endl;
    }
}

void printVec(vector<string> &vec) {
    try {
        cout << "Size of Vector : " << vec.size() << endl;  // vec.size() O(1) 
        cout << "[";
        for (int i = 0; i < vec.size(); i++) {
            cout << vec[i];
            if (i != vec.size()-1)
                cout << ", ";
        }
        cout << "]" << endl;

    }catch (exception &e) {
        cout << "PrintVec Error : " << e.what() << endl;
    }
}

