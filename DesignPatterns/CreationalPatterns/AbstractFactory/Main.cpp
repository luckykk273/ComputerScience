#include <iostream>

#include "AbstractFactory.h"


int main()
{
	// Clients create parts solely through the part factory interface;
	// Clients have no knowledge of the classes that implement parts for a particular style;
	PartFactory* fac;
	Mouse* mouse;
	Keyboard* kb;

	// If clients want to create Windows style parts:
	fac = new WindowsFactory();
	mouse = fac->CreateMouse();
	kb = fac->CreateKeyboard();

	std::cout << "Windows style parts: " << std::endl;
	std::cout << mouse->GetName() << ", " << kb->GetName() << std::endl;

	// If clients want to create Mac style parts:
	fac = new MacFactory();
	mouse = fac->CreateMouse();
	kb = fac->CreateKeyboard();

	std::cout << "\nMac style parts: " << std::endl;
	std::cout << mouse->GetName() << ", " << kb->GetName() << std::endl;

	delete fac, mouse, kb;
}