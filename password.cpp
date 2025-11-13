#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main() {
    string pass = "";
    const int length = 16;

    srand(time(nullptr));

    for (int i = 0; i < length; i++) {
        int num = 33 + (rand() % 94);
        pass += static_cast<char>(num);
    }

    cout << "password: " << pass << endl;
    return 0;
}
