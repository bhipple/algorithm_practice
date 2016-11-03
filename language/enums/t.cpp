#include <iostream>

namespace Foo {
enum Bar {
    La, Dee, Da
};
}

namespace {
Foo::Bar toFoo(int x) {
    return static_cast<Foo::Bar>(x);
}
}

int main() {
    Foo::Bar x = Foo::Dee;
    std::cout << x << std::endl;

    Foo::Bar y = toFoo(2);
    std::cout << y << std::endl;

    // Out of range?
    Foo::Bar z = toFoo(5);
    std::cout << z << std::endl;

}
