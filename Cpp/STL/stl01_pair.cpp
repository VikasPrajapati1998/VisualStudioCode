#include <bits/stdc++.h>

/*
STL : Standard Template Library
A. Container
    Data Structure, which is pre-in-build in C++.
    (I): Sequential Container
        1. Vectors
        2. Stack
        3. Queue
        4. Pair(Not a Container)
    (II): Ordered
        1. Maps
        2. Multimaps
        3. Set
        4. Multisets
    (III): Unordered
        1. Unordered Map
        2. Unordered Set
    (IV): Nested Containers
        1. vector<vector<int>>
        2. map<int, vector<int>>
        3. set<pair<int, string>>
        4. vector<map<int, set<int>>>

B. Iterator
    - Similar to pointers
    - begin(), end()
    - vector<int>::iterator it;
    - continuity for containers

C. Algorithms
    - Upper Bound
    - Lower Bound
    - Sort (Comparator)
    - Max - element
    - Min - element
    - accumulate
    - reverse
    - count
    - find
    - Next permutations
    - pre permutations

D. Functors 
    Classes in cpp which can act as functions.

*/

using namespace std;

int main(int argc, char *argv[]) {
    // Pair
    pair<int, string> p;
    p = make_pair(2, "abc");
    cout << p.first << " " << p.second << endl;

    pair<int, string> p1;
    p1 = {3, "alphap"};
    cout << p1.first << " " << p1.second << endl;

    pair<int, string> p2 = p;
    p2.first = 7;
    p2.second = "beta";
    cout << p2.first << " " << p2.second << endl;
    cout << p.first << " " << p.second << endl;

    pair<int, string> &p3 = p;
    p3.first = 9;
    p3.second = "Gama";
    cout << p3.first << " " << p3.second << endl;
    cout << p.first << " " << p.second << endl;

    // array of pairs
    int arr1[] = {1, 2, 3};
    int arr2[] = {2, 3, 4};

    pair<int, int> p_array[3];
    p_array[0] = {1, 2};
    p_array[1] = {2, 3};
    p_array[2] = {3, 4};
    swap(p_array[0], p_array[2]);
    for (int i=0; i<3; i++)
        cout << "(" << p_array[i].first << ", " << p_array[i].second << ")" << endl;



    return 0;
}

