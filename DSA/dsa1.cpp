#include<iostream>
using namespace std;
class A{
public:
    int number;
    A(){
        number = 0;
    }
    A(A& a){
        cout << "I am Copy Constructor" << endl;
        this->number = a.number;
    }
// private:
//     int numberPriv;
};
class B:public A{
public:
    string number;
};
int main(){
    A* a = new A();
    A d = *a;
    d.number=5;
    a->number = 1;
    // b->number = 2;
    a->number = 3;
    cout << a->number << d.number;
    return 0;
}