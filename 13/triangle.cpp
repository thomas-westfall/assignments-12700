#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;
std::string line(int l, std::string c){
  std::string ans = "";
  for(int i = 0; i < l; i++){
    ans = ans + c;
  }
  return ans;
}

std::string rect(int w, int h) {
  std::string ans = "";
  for (int i = 0; i < h - 1; i++){
    for (int j = 0; j < w; j++){
      ans = ans + "*";
    }
    ans = ans + "\n";
  }
  return ans;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  std::string ans = "";
  for (int i = 1; i <= h; i++){
    for (int j = 1; j <= i; j++){
      ans = ans + "*";
    }
    ans = ans + "\n";
  }

  return ans;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  std::string ans = "";
  for (int i = 1; i <= h; i++){
    for (int j = h - 1; j >= i; j--){
      ans = ans + " ";
    }
    for (int k = 1; k <= (2 * i - 1);k++){
      ans = ans + "*";
    }
       ans = ans + "\n";
  }
  return ans;
}
  

/*
  *
 **
***
 */
std::string tri3(int h) {
  std::string ans = "";
  int k = 0;
  int o = 1;
  for (int i = 0; i < h; i++){
      for (int j = 0; j < h - k; j++){
      ans = ans + " ";
      }
      for (int z = 0; z < o; z++){
      ans = ans + "*";
     }
      k = k + 1;
      o = o + 1;
    ans = ans + "\n";
  }				 

  
  return ans;
}

int main(){
  string s="hello";
  cout<<s<<endl;
  cout<<line(5,"c")<<endl;
  cout<<rect(2,4)<<endl;
  cout<<tri1(5)<<endl;
  cout<<tri2(5)<<endl;
  cout<<tri3(5)<<endl;
}
