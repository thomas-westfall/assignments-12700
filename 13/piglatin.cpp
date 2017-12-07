#include <iostream>
#include <string>
#include <algorithm>
using std::cout;
using std::endl;
using std::string;
using std::find;
std::string piglatinify(std::string s){
  std::string ans = "";
  string vowels[5] = {"a","e","i","o","u"};
  std::string c = s.substr(0,1);
  std::string *begin = vowels;
  std::string *end = vowels + 5;


  if (std::find(begin, end, c) != end){
      ans = s + "ay";
  }
  else{
    ans = s.substr(1,s.length() - 1) + c + "ay";
  }
  
  return ans;
}



int main(){
  string s="hello";
  string o="okay";
  
  cout<<piglatinify(s)<<endl;
  cout<<piglatinify(o)<<endl;
 
}
