// Find_Max.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <algorithm>
#include <stdlib.h>

extern C find_maxasm(float* val, int len);

float get_max(float *val, int len) {
    if (len == 0) {
        return NULL;
    }
    float max = val[0];
    for (int i = 1; i < len; i++) {
        if (val[i] > max) max = val[i];
   }
    return max;
}

int main()
{
    float teste[6] = { 0.1,0.2,1.0,1.1,0.2,0.1};
    float p = get_max(teste,6);
    float* g;
    g = std::max_element(teste,teste+6);
    std::cout << "Maximo: " << p << "\n";
    std::cout << "Maximo2: " << *g;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
