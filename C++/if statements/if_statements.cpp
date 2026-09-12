#include <iostream>
#include <string>

int main(){
    std::string name;
    std::string password;
    int tries = 0;
    std::cout <<"Enter name: " << std::endl ;
    std::cin >>name;
    std::cout<<"Enter password:" << std::endl ;
    std::cin >>password;
    while (password != "Bleh:3" && name != "Duckie")
    {
        tries++;
        std::cout <<"Wrong password or name. Try again."<< std::endl;
        std::cout << "You've got " << 5 - tries << " tries left" << std::endl ;
        std::cout <<"Enter name: " << std::endl ;
        std::cin >>name;
        std::cout <<"Enter password:" << std::endl ;
        std::cin >>password;
        if (tries == 5)
        {
            std::cout << "Locked out. Try again later." << std::endl;
            break;
        }
    }
    std::cout <<"Ya got in. Yipperssss:D";
}