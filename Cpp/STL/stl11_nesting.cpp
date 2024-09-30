#include <bits/stdc++.h>

using namespace std;

#define DEBUG 4


int main(int argc, char *argv[]) {
    #if defined(DEBUG) && DEBUG == 1
    {
        // map
        // map<int, int> m;
        map<pair<int, int>, int> mp;

        // compate pairs : first compare key and pair
        pair<int, int> p1, p2, p3, p4;
        p1 = {1, 2};
        p2 = {2, 3};
        p3 = {2, 4};
        p4 = {2, 1};
        std::cout << "p1 < p2 = " << (p1 < p2) << std::endl;
        std::cout << "p2 < p3 = " << (p2 < p3) << std::endl;
        std::cout << "p4 < p2 = " << (p4 < p2) << std::endl;
        std::cout << std::endl;

        mp[p1] = 18254;
        mp[p2] = 18263;
        mp[p3] = 18239;
        mp[p4] = 18255;

        for (auto &val : mp) {
            std::cout << "(" << val.first.first << ", " << val.first.second << ") : " << val.second << std::endl; 
        }
        std::cout << std::endl;

        // compate set : compare elementwise
        map<set<int>, int> ms;
        set<int> s1 = {1, 2, 3};
        set<int> s2 = {2, 3};
        std::cout << "s1 < s2 = " << (s1 < s2) << std::endl;

    }

    #elif defined(DEBUG) && DEBUG == 2
    {
        // map of pair and vector
        map<pair<string, string>, vector<int>> mpv;
        int map_size = 0;
        std::cout << "Enter Size of Map: "; std::cin.sync(); std::cin >> map_size;
        
        int i;
        for (i=0; i<map_size; i++) {
            string first, second;
            std::cout << i+1 << ": Pair: " << std::endl;
            std::cout << "Enter first: " << first; std::cin.sync(); std::cin >> first;
            std::cout << "Enter second: " << second; std::cin.sync(); std::cin >> second;

            int vec_size, j, value;
            std::cout << "Enter Size of Vector: "; std::cin.sync(); std::cin >> vec_size;
            for (j=0; j<vec_size; j++) {
                std::cout << "Enter " << j+1 << " value: "; std::cin.sync(); std::cin >> value;
                mpv[{first, second}].push_back(value);
            }
        }

        // print map
        for(auto &pr: mpv) {
            auto &full_name = pr.first;
            auto &list = pr.second;
            std::cout << full_name.first << " " << full_name.second << ": ";
            for (auto &element: list) {
                std::cout << element << ", ";
            }
            std::cout << std::endl;
        }
    }

    #elif defined(DEBUG) && DEBUG == 3
    {
        // set of pair and vector
        set<pair<string, string>> sv;
        int set_size = 0;
        std::cout << "Enter Size of Set: "; std::cin.sync(); std::cin >> set_size;
        
        int i;
        for (i=0; i<set_size; i++) {
            string first, second;
            std::cout << i+1 << ": Pair: " << std::endl;
            std::cout << "Enter first: " << first; std::cin.sync(); std::cin >> first;
            std::cout << "Enter second: " << second; std::cin.sync(); std::cin >> second;
            sv.insert({first, second});
            std::cout << std::endl;
        }
        std::cout << std::endl;

        // print set
        std::cout << "Print set of pairs : ";
        for(auto &pr: sv) {
            std::cout << pr.first << " " << pr.second << ", ";
        }
        std::cout << std::endl;
    }

    #elif defined(DEBUG) && DEBUG == 4
    {
        map<int, set<string>> students;

        int test_case;
        std::cout << "Enter test_case: "; std::cin.sync(); std::cin >> test_case;

        // insert value in map
        for (int i=0; i<test_case; i++) {
            string name; int marks;
            std::cout << i+1 << ". Enter Name and Marks: "; std::cin.sync(); std::cin >> name >> marks;
            students[marks].insert(name);
        }
        std::cout << std::endl;

        // Print map
        for (const auto &val : students) {
            std::cout << "Marks: " << val.first << " | Students: ";
            for (const auto &student_name : val.second) {
                std::cout << student_name << " ";
            }
            cout << endl;
        }
        std::cout << std::endl;

        // Print the map in the desired format
        for (auto it = students.begin(); it != students.end(); ++it) {
            for (const auto& student_name : it->second) {
                std::cout << student_name << " " << it->first << std::endl;
            }
        }
        std::cout << std::endl;

        // Print the map in the desired format
        for (auto it = students.rbegin(); it != students.rend(); ++it) {
            for (const auto& student_name : it->second) {
                std::cout << student_name << " " << it->first << std::endl;
            }
        }
        std::cout << std::endl;




    }

    #endif

    return 0;
}


