#include <iostream>
#include <string>
#include <cstring>

using namespace std;

string pixelToBit(const int* array, const size_t size) {
    string bits;

    for (int i = 0; i < size; ++i) {
        bits += to_string(static_cast<int>(round(array[i] / 255.0)) > 0.5 ? 1 : 0);
    }

    return bits;
}

void appendNTimes(string& s1, const string& s2, int n) {
    for (int i = 0; i < n; i++) {
        s1 += s2;
    }
}

string expandSlab(const string& slab, int exp, int width) {
    string op1;
    // Horizontal expansion
    for (char s : slab) {
        op1.append(exp, s);
    }
    
    int n = op1.length();
    string op2;
    // Vertical expansion
    for (int i = 0; i < n; i += width) {
        appendNTimes(op2, op1.substr(i, width), exp);
    }

    return op2;
}

extern "C" {
    const char* c_pixelToBit(const int* array, const size_t size) { 
        string bits = pixelToBit(array, size); 
        return bits.c_str();
    }
    const char* c_expandSlab(const char* slab, int exp, int width) {
        string result = expandSlab(slab, exp, width);
        char* c_string = new char[result.size() + 1];
        strcpy(c_string, result.c_str());
        return c_string;
    }
}

// g++ -fPIC -shared DataProccessing/cLibs/helper.cpp -o DataProccessing/cLibs/c_lib.so