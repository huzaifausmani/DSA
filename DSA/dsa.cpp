#include <iostream>
#include <stdlib.h>
using namespace std;
class Car
{
public:
    int petrolConsumption;
    Car() { cout << "Car Constructing..." << endl; }
    virtual void start() { cout << "Car Starting...!" << endl; }
    virtual void drive() { cout << "Car Driving...!" << endl; }
    virtual ~Car() { cout << "Car Destroying..." << endl; }
};
class SuperCar : public Car
{
public:
    int petrolConsumption;
    SuperCar() { cout << "SuperCar Constructing..." << endl; }
    void start() { cout << "SuperCar Starting...!" << endl; }
    void drive() { cout << "SuperCar Driving...!" << endl; }
    virtual void drive2() { cout << "SuperCar Driving...!" << endl; }
    ~SuperCar() { cout << "SuperCar Destroying..." << endl; }
};
class VintageCar : public Car
{
public:
    int petrolConsumption;
    VintageCar() { cout << "VintageCar Constructing..." << endl; }
    ~VintageCar() { cout << "VintageCar Destroying..." << endl; }
};
int main()
{
    // creating children
    cout << "Creating First Child SuperCar" << endl;
    SuperCar *super = new SuperCar();

    cout << "\nCreating First Child VintageCar" << endl;
    VintageCar *vintage = new VintageCar();

    // Creating Parent and assigning first child
    Car *car = new Car();
    car = super;
    car->drive();
    car->petrolConsumption = 9;

    car = nullptr;
    delete super;
    car = vintage;
    cout << "\nDestroying Parent" << endl;
    delete car;
    // car = &super;
    // car->drive();
    // car->start();
    // SuperCar super;
    return 0;
}
// solving diamond problem with virtual keyword