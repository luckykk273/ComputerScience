#include <iostream>
#include <string>
#include <stdexcept>

#include "AbstractFactory.h"


int main()
{
	AbstractFactory* fac;
	Button* btn;
	Border* bdr;
		
	std::cout << "Please choose the operation system: " << std::endl;
	std::string system;
	std::cin >> system;
	try 
	{
		if (system == "MAC")
		{
			fac = new MacFactory();
		}
		else if (system == "WIN")
		{
			fac = new WinFactory();
		}
		else
		{
			throw std::invalid_argument("Only `MAC` or `WIN` provided!");
		}
	}
	catch (const std::invalid_argument& e)
	{
		std::cerr << e.what() << std::endl;
		return -1;
	}

	btn = fac->CreateButton();
	bdr = fac->CreateBorder();

	std::cout << btn->GetName() << std::endl;
	std::cout << bdr->GetName() << std::endl;

	delete fac, btn, bdr;
}