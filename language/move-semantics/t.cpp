#include <iostream>
#include <vector>
#include <stdlib.h>

// See slide 28 of this presentation for an overview of which special members
// are or are not provided by the compiler, depending on which special members
// the user declares.
// https://howardhinnant.github.io/bloomberg_2016.pdf
class Foo {
  public:
    Foo() {
        x = rand();
        std::cout << "Constructed a Foo with x = " << x << " at " << this << std::endl;
        y = std::to_string(x);
    }

    Foo(const Foo& other): x(other.x), y(other.y) {
        std::cout << "Copied a Foo " << std::endl;
    }

    Foo(Foo&& other) noexcept: x(other.x), y(other.y) {
        std::cout << "Moved a Foo " << std::endl;
    }

    Foo& operator=(const Foo& other) {
        std::cout << "operator= copy a Foo" << std::endl;
        Foo tmp(other);
        *this = std::move(tmp);
        return *this;
    }

    Foo& operator=(const Foo&& other) noexcept {
        std::cout << "operator= move a Foo" << std::endl;
        x = other.x;
        y = other.y;
        return *this;
    }

    int x;
    std::string y;
};

std::vector<Foo> getFoos(size_t ct) {
    std::vector<Foo> vf(ct);
    return vf;
}

std::vector<Foo> movingFoos(size_t ct) {
    std::vector<Foo> vf;
    vf.reserve(ct);
    for(size_t i = 0; i < ct; ++i) {
        Foo f;
        vf.push_back(std::move(f));
    }
    return vf;
}

int main() {
    Foo f;

    std::cout << "\n****************************************\n\n";
    Foo g = std::move(f);
    std::cout << "^ Moved f to g with x = " << g.x << " at " << &g << std::endl;

    Foo h = f;
    std::cout << "^ Valid but unspecified state: h.x from f: " << h.x << std::endl;

    std::cout << "\n****************************************\n\n";
    std::vector<Foo> vf = getFoos(5);
    std::cout << "^ Vector of 5 Foos returned from function at " << &vf << std::endl;

    std::cout << "\n****************************************\n\n";
    std::vector<Foo> vf2 = movingFoos(5);
    std::cout << "^ Vector from movingFoos at " << &vf2 << std::endl;
}
