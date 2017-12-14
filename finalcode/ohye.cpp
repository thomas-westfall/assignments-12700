#include <iostream>
#include <string>
#include <algorithm>
using std::cout;
using std::endl;
using std::string;
using std::find;


int paper_needed(int l,int w,int h){
  int ans = 0;
  int temparea = 0;
  int areaa = l * w;
  int areab = l * h;
  int areac = w * h;
  int aread = 0;

  if (areaa <= areab){
    aread = areaa;
  }
  if (areab <= areaa){
    aread = areab;
  }
  if (areac <= aread){
    aread = areac;
      }
  int min = aread;

  
  ans = ans + ((2 * l * w) + (2 * w * h) + (2 * h * l));
  ans = ans + min;
  return ans;
}


int ribbon_needed(int l, int w, int h){
  int ans = 0;
  int min = 0;
  int secondmin = 0;
  int x = 0;


  if (l <= w){
    x = l;
  }
  else{
    x = w;
  }
  
  if (x <= h){
    min = x;
  }
  else{
    min = h;
    secondmin = x;
  }
  if ((h <= l) or (h <= w)){
    secondmin = h;
  }
  
  //ans = ans + ((2 * min) + (2 * secondmin) + 5);

  ans = secondmin;
  return ans;
  
}


int main(){
  cout<<paper_needed(2,3,4)<<endl;
  cout<<ribbon_needed(2,3,4)<<endl;

}
