#include <iostream>
#include <string>

using namespace std;

int main() {

    string text;

    cout << "Enter Text: ";
    cin >> text;

    // ---------------- Rail Fence Cipher ----------------

    string even = "", odd = "";

    int index = 0;

    // Encryption
    for(char c : text) {

        if(index % 2 == 0)
            even += c;
        else
            odd += c;

        index++;
    }

    string railCipher = even + odd;

    cout << "\nRail Fence Encrypted Text: " << railCipher << endl;

    // Decryption
    string railDecrypt = "";

    int mid = (text.length() + 1) / 2;

    int e = 0, o = mid;

    for(int i = 0; i < text.length(); i++) {

        if(i % 2 == 0)
            railDecrypt += railCipher[e++];
        else
            railDecrypt += railCipher[o++];
    }

    cout << "Rail Fence Decrypted Text: " << railDecrypt << endl;


    // ---------------- Columnar Transposition Cipher ----------------

    int key;

    cout << "\nEnter Key for Columnar Cipher: ";
    cin >> key;

    string columnCipher = "";

    // Encryption
    for(int col = 0; col < key; col++) {

        for(int i = col; i < text.length(); i += key) {
            columnCipher += text[i];
        }
    }

    cout << "Columnar Encrypted Text: " << columnCipher << endl;

    // Decryption
    string columnDecrypt(text.length(), ' ');

    index = 0;

    for(int col = 0; col < key; col++) {

        for(int i = col; i < text.length(); i += key) {
            columnDecrypt[i] = columnCipher[index++];
        }
    }

    cout << "Columnar Decrypted Text: " << columnDecrypt << endl;

    return 0;
}