#include <iostream>
using namespace std;

bool withdrawalMachine(int amount){
    if(amount % 10 != 0){return false;}
    else{
        int note50, note20, note10;
        double other;
        note50 = amount / 50;
        other = amount - (note50 * 50);
        note20 = other / 20;
        other = other - (note20 * 20);
        note10 = other / 10;
        cout<< endl << note50 <<" $50 notes, " << note20 << " $20 notes, " << note10 << " $10 notes."<< endl;
        return true;
    }
}

int main(){
    withdrawalMachine(43);
    return 0;
}


