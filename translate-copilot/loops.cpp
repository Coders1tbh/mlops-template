// C++ version
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> fruits = {"apple", "banana", "pear"};
    for (const auto& fruit : fruits) {
        std::cout << "I like " << fruit << std::endl;
    }
    return 0;
}
