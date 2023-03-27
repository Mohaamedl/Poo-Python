//#include <iostream>
//#include <iomanip>
using namespace std;
int main() {
  float num=8.28478; //6 significant figures
  
  cout<<setprecision(1)<<num<<endl;   //1 significant figures
  cout<<setprecision(2)<<num<<endl;   //2 significant figures
  cout<<setprecision(3)<<num<<endl;   //3 significant figures
  cout<<setprecision(4)<<num<<endl;   //4 significant figures
  cout<<setprecision(5)<<num<<endl;   //5 significant figures
  cout<<setprecision(6)<<num<<endl;   //6 significant figures
  
  
  return 0;
};