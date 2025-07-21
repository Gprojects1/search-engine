#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
#include <clocale>

using namespace std;

bool is_cyrillic(unsigned char c) {
    return (c >= 0xD0 && c <= 0xDF) || (c >= 0x80 && c <= 0xBF);
}

vector<string> extract_words(const string& filename) {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    vector<string> words;
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error: Could not open file " << filename << endl;
        return words;
    }

    string word;
    char c;
    while (file.get(c)) {
        unsigned char uc = static_cast<unsigned char>(c);
        if (isalpha(uc) || isdigit(uc) || is_cyrillic(uc)) {
            word += tolower(uc);
        } else if (!word.empty()) {
            words.push_back(word);
            word.clear();
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }

    return words;
}

int count_word_pairs(const vector<string>& words, const string& word1, const string& word2, int max_distance) {
    int count = 0;
    size_t last_pos = string::npos; 
    
    for (size_t i = 0; i < words.size(); ++i) {
        if (words[i] == word1) {
            for (size_t j = i + 1; j < words.size() && j <= i + max_distance + 1; ++j) {
                if (words[j] == word2 && (last_pos == string::npos || j > last_pos)) {
                    count++;
                    last_pos = j; 
                    break; 
                }
            }
        }
    }
    return count;
}

int main(int argc, char* argv[]) {
    if (argc != 5) {
        cerr << "Usage: " << argv[0] << " <filename> <word1> <word2> <max_distance>" << endl;
        return 1;
    }

    string filename = argv[1];
    string word1 = argv[2];
    string word2 = argv[3];
    int max_distance;
    try {
        max_distance = stoi(argv[4]);
    } catch (...) {
        cerr << "Error: max_distance must be an integer" << endl;
        return 1;
    }

    transform(word1.begin(), word1.end(), word1.begin(), ::tolower);
    transform(word2.begin(), word2.end(), word2.begin(), ::tolower);

    vector<string> words = extract_words(filename);
    if (words.empty()) {
        return 1;
    }

    int result = count_word_pairs(words, word1, word2, max_distance);
    cout << result << endl;

    return 0;
}