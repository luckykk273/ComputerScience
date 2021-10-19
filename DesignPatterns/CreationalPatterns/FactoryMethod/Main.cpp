#include <iostream>

#include "FactoryMethod.h"


int main()
{
	// Clients create parts solely through the particualr factory interface;
	MouseFactory* mf;
	KeyboardFactory* kf;
	Mouse* mouse;
	Keyboard* kb;

	// If clients want to create Windows style parts:
	mf = new WindowsMouseFactory();
	kf = new WindowsKeyboardFactory();
	mouse = mf->CreateMouse();
	kb = kf->CreateKeyboard();

	std::cout << "Windows style parts: " << std::endl;
	std::cout << mouse->GetName() << ", " << kb->GetName() << std::endl;

	// If clients want to create Mac style parts:
	mf = new MacMouseFactory();
	kf = new MacKeyboardFactory();
	mouse = mf->CreateMouse();
	kb = kf->CreateKeyboard();

	std::cout << "\nMac style parts: " << std::endl;
	std::cout << mouse->GetName() << ", " << kb->GetName() << std::endl;

	delete mf, kf, mouse, kb;
}