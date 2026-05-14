#include <iostream>
#include <string>
using namespace std;

int main() {
    string plaintext;
    int key;

    cout << "Enter Plain Text: ";
    cin >> plaintext;

    cout << "Enter mod factor (integer key): ";
    cin >> key;

    string ciphertext = "";
    string decrypted = "";

    // Encrypt using XOR
    for (char ch : plaintext) {
        char enc = ch ^ key;   // bitwise XOR
        ciphertext += enc;
    }

    cout << "Ciphertext: " << ciphertext << endl;

    for (char ch : ciphertext) {
        char dec = ch ^ key;
        decrypted += dec;
    }

    cout << "Decrypted text: " << decrypted << endl;

    return 0;
}
