#include <iostream>

using namespace std;

string pixelToBit(const int* array, const size_t size) {
    string bits;

    for (int i = 0; i < size; ++i) {
        bits += to_string(static_cast<int>(round(array[i] / 255.0)) > 0.5 ? 1 : 0);
    }

    return bits;
}

extern "C" {
    const char* c_pixelToBit(const int* array, const size_t size) { 
        string bits = pixelToBit(array, size); 
        return bits.c_str();
    }
}

// g++ -fPIC -shared DataProccessing/cLibs/helper.cpp -o DataProccessing/cLibs/c_lib.so