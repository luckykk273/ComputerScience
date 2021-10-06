#include <string>
#include <stdexcept>

#include "CreationalPatterns/include/AbstractFactory.h"


int main()
{
	AbstractFactory* fac;
	Button* btn;
	Border* bdr;

	std::string style;
	std::cin >> style;
	try 
	{
		if (style == "MAC")
		{
			fac = new MacFactory();
		}
		else if (style == "WIN")
		{
			fac = new WinFactory();
		}
		else
		{
			throw std::invalid_argument("No such type!");
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