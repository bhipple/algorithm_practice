#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1,2,3,4,5};

    const auto itr = v.begin();
    (*itr) *= 10;
    // Won't compile, since the iterator itself is constant.
    // ++itr;

    auto citr = v.cbegin();
    // won't compile, since the iterator points to a constant value
    //(*citr)++;
    ++citr;

    std::cout << v[0] << std::endl;
    std::cout << *itr << std::endl;
    std::cout << *citr << std::endl;
}
