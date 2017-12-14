#include <string>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <array>

using std::cout;
using std::endl;
using std::string;
using std::find;



// sample data - you can add more
int data[] = {5,3,19,12,15,19,33,21,1,5,26,7,8,14,18};


int sum(int data[], int size){
  int ans = 0;
  for (int i = 0; i < size; i++){
    ans = ans + i;
  }
  return ans;
  
}

int sum_odd(int data[], int size){
  return 0;
}


int main(){
  cout<<sum(data,10)<<endl;
  cout<<sum_odd(data,10)<<endl;

}
