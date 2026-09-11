#include <iostream>
int main(){
    int x,y;
    int result=35;
    char comma;
    std::cout<<"Hewwo. Pick numbers sparated by commas:3 ";
    std::cin>>x>>comma>>y;
    result+=x+y;
    std::cout<<"The result is: "<<result;
    return 0;
}