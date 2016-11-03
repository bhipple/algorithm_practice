#include <iostream>
#include <vector>
#include <stdlib.h>

class Foo {
  public:
    Foo() {
        x = rand();
        std::cout << "Constructed a Foo with x = " << x << " at " << this << std::endl;
        y = std::to_string(x);
    }

    int x;
    std::string y;
};

std::vector<Foo> getFoos(int ct) {
    std::vector<Foo> vf(ct);
    return vf;
}

std::vector<Foo> movingFoos(int ct) {
    std::vector<Foo> vf;
    for(size_t i = 0; i < ct; ++i) {
        Foo f;
        vf.push_back(std::move(f));
    }
    return vf;
}

int main() {
    Foo f;

    Foo g = std::move(f);
    std::cout << "Moved f to g with x = " << g.x << " at " << &g << std::endl;

    Foo h = f;
    std::cout << "Valid but unspecified state: h.x from f: " << h.x << std::endl;


    std::vector<Foo> vf = getFoos(5);
    std::cout << "^ Vector of 5 Foos returned from function at " << &vf << std::endl;

    std::vector<Foo> vf2 = movingFoos(5);
    std::cout << "^ Vector from movingFoos at " << &vf2 << std::endl;
}
