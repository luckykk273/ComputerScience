#include <iostream>

#include "Builder.h"

int main()
{
	Computer* computer;
	ComputerDirector* computer_director;

	// If clients want to build a Windows computer:
	WindowsComputerBuilder* windows_computer_builder = new WindowsComputerBuilder();
	computer_director = new ComputerDirector(windows_computer_builder);
	computer_director->CreateComputer("Windows");
	computer = windows_computer_builder->GetComputer();

	std::cout << "\n";

	// If clients want to build a Mac computer:
	MacComputerBuilder* mac_computer_builder = new MacComputerBuilder();
	computer_director = new ComputerDirector(mac_computer_builder);
	computer_director->CreateComputer("Mac");
	computer = mac_computer_builder->GetComputer();
}