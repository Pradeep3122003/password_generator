#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int length = 16;

    if (argc > 1) {
        length = atoi(argv[1]);
        if (length <= 0) {
            cout << "Invalid length!" << endl;
            return 1;
        }
    }

    string pass = "";
    srand(time(nullptr));

    for (int i = 0; i < length; i++) {
        int num = 33 + (rand() % 94);
        pass += static_cast<char>(num);
    }

    cout << "password: " << pass << endl;
    return 0;
}
