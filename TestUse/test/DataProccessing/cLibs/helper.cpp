#include <iostream>
#include <string>
#include <cstring>
#include <cstdint>
#include <unordered_map>

using namespace std;

string pixelToBit(const uint8_t* pix, const size_t height, const size_t width) {
    string bits;

    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; j++) {
            bits += to_string(static_cast<int>(round(pix[i * width + j] / 255.0)) > 0.5 ? 1 : 0);
        }
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

int max_char(const string& string) {
    unordered_map<char, int> char_counts;
    for (char c : string) {
        char_counts[c]++;
    }
    
    int max_count = 0;
    for (const auto& pair : char_counts) {
        max_count = max(max_count, pair.second);
    }
    
    return (char_counts['1'] == max_count) ? 1 : 0;
}

string compressSlab(const string& slab, int exp, int width, int pixel_count) {
    string op;
    int vchunk_size = exp * width;
    
    for (int i = 0; i < pixel_count; i += vchunk_size) {
        string vslab = slab.substr(i, vchunk_size);
        
        for (int j = 0; j < width; j += exp) {
            string t_op;
            
            for (int k = 0; k < exp; k++) {
                for (int l = 0; l < exp; l++) {
                    int index = j + k * width + l;
                    t_op += vslab[index];
                }
            }
            
            op += to_string(max_char(t_op));
        }
    }
    
    return op;
}

const char* toCString(string s) {
    char* c_string = new char[s.size() + 1];
    strcpy(c_string, s.c_str());
    return c_string;
}

extern "C" {
    const char* c_pixelToBit(const uint8_t* array, const size_t height, const size_t width) {
        return toCString(pixelToBit(array, height, width));
    }
    const char* c_expandSlab(const char* slab, int exp, int width) {
        return toCString(expandSlab(slab, exp, width));
    }
    const char* c_compressSlab(const char* slab, int exp, int width, int pixel_count) {
        return toCString(compressSlab(slab, exp, width, pixel_count));
    }
}

// g++ -fPIC -shared DataProccessing/cLibs/helper.cpp -o DataProccessing/cLibs/c_lib.so