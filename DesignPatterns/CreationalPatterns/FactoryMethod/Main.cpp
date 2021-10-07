#include <iostream>
#include <string>
#include <stdexcept>

#include "FactoryMethod.h"

int main()
{
	/*
	 In factory method, every factory produces the products more specifically than the factory in abstract factory.
	 Every product has its own factory to produce;
	 (e.g. Mac button factory can only produce the Mac button.)

	 In abstract factory, one factory can produce a whole product family.
	 (e.g. Mac factory can produce both the Mac button and the Mac border.)
	*/
	std::cout << "Please choose the operation system: " << std::endl;
	std::string system;
	std::cin >> system;
	std::cout << "Please choose the product: " << std::endl;
	std::string product;
	std::cin >> product;

	try
	{
		if (system == "MAC" && product == "Button")
		{
			MacButtonFactory* fac = new MacButtonFactory();
			Button* btn = fac->CreateButton();
			std::cout << btn->GetName() << std::endl;
		}
		else if (system == "MAC" && product == "Border")
		{
			MacBorderFactory* fac = new MacBorderFactory();
			Border* bdr = fac->CreateBorder();
			std::cout << bdr->GetName() << std::endl;
		}
		else if (system == "WIN" && product == "Button")
		{
			WinButtonFactory* fac = new WinButtonFactory();
			Button* btn = fac->CreateButton();
			std::cout << btn->GetName() << std::endl;
		}
		else if (system == "WIN" && product == "Border")
		{
			WinBorderFactory* fac = new WinBorderFactory();
			Border* bdr = fac->CreateBorder();
			std::cout << bdr->GetName() << std::endl;
		}
		else
		{
			throw std::invalid_argument(std::string("Only `MAC` or `WIN` provided in the operation system;\n")
									  + std::string("Only `Button` or `Border` provided in the product;\n"));
		}
	}
	catch (const std::invalid_argument& e)
	{
		std::cerr << e.what() << std::endl;
		return -1;
	}

	/*
	 Of course factory method can peform as like the abstract factory;
	 The clients can only determine which operation system they want and delegate to two specific factories in the backend.
	 */
	Button* btn;
	Border* bdr;

	std::cout << "Please choose the operation system: " << std::endl;
	std::string system2;
	std::cin >> system2;
	try
	{
		if (system2 == "MAC")
		{
			MacButtonFactory* buttonFac = new MacButtonFactory();
			MacBorderFactory* borderFac = new MacBorderFactory();
			btn = buttonFac->CreateButton();
			bdr = borderFac->CreateBorder();
		}
		else if (system2 == "WIN")
		{
			WinButtonFactory* buttonFac = new WinButtonFactory();
			WinBorderFactory* borderFac = new WinBorderFactory();
			btn = buttonFac->CreateButton();
			bdr = borderFac->CreateBorder();
		}
		else
		{
			throw std::invalid_argument(std::string("Only `MAC` or `WIN` provided in the operation system;\n")
				+ std::string("Only `Button` or `Border` provided in the product;\n"));
		}

		std::cout << btn->GetName() << std::endl;
		std::cout << bdr->GetName() << std::endl;
	}
	catch (const std::invalid_argument& e)
	{
		std::cerr << e.what() << std::endl;
		return -1;
	}
}