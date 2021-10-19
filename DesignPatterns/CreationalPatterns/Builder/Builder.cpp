#include <iostream>

#include "Builder.h"


/*******************************************************************
 * Define the three parts of the computer: mouse, keyboard, screen *
 * Each part has two styles:               Windows, Mac            *
 *******************************************************************/
const char* WindowsMouse::GetName() const { return "WindowsMouse"; }
const char* MacMouse::GetName() const { return "MacMouse"; }

const char* WindowsKeyboard::GetName() const { return "WindowsKeyboard"; }
const char* MacKeyboard::GetName() const { return "MacKeyboard"; }

const char* WindowsScreen::GetName() const { return "WindowsScreen"; }
const char* MacScreen::GetName() const { return "MacScreen"; }


/**************************************
 * Define the final product: computer *
 **************************************/
void Computer::AddMouse(Mouse* mouse) { std::cout << mouse->GetName() << " is added." << std::endl; }
void Computer::AddKeyboard(Keyboard* kb) { std::cout << kb->GetName() << " is added." << std::endl; }
void Computer::AddScreen(Screen* screen) { std::cout << screen->GetName() << " is added." << std::endl; }


/**************************************************
 * Define the two computer builders: Windows, Mac *
 **************************************************/
void WindowsComputerBuilder::BuildComputer() { m_Computer = new Computer(); }
void WindowsComputerBuilder::BuildMouse() { m_Computer->AddMouse(new WindowsMouse()); }
void WindowsComputerBuilder::BuildKeyboard() { m_Computer->AddKeyboard(new WindowsKeyboard()); }
Computer* WindowsComputerBuilder::GetComputer()
{
	std::cout << "Final product: Windows computer." << std::endl;
	return m_Computer;
}

void MacComputerBuilder::BuildComputer() { m_Computer = new Computer(); }
void MacComputerBuilder::BuildMouse() { m_Computer->AddMouse(new MacMouse()); }
void MacComputerBuilder::BuildKeyboard() { m_Computer->AddKeyboard(new MacKeyboard()); }
void MacComputerBuilder::BuildScreen() { m_Computer->AddScreen(new MacScreen()); }
Computer* MacComputerBuilder::GetComputer()
{
	std::cout << "Final product: Mac computer." << std::endl;
	return m_Computer;
}

/********************************
 * Define the computer director *
 ********************************/
ComputerDirector::ComputerDirector(ComputerBuilder* cb) : m_ComputerBuilder(cb) {}
void ComputerDirector::CreateComputer(const char* style)
{
	if (style == "Windows")  // If Windows computer is created
	{
		std::cout << "Windows computer starts to create..." << std::endl;
		m_ComputerBuilder->BuildComputer();

		// Suppose Windows computer only contains mouse and keyboard;
		m_ComputerBuilder->BuildMouse();
		m_ComputerBuilder->BuildKeyboard();

	}
	else  // If Mac computer is created
	{
		std::cout << "Mac computer starts to create..." << std::endl;
		m_ComputerBuilder->BuildComputer();

		// Suppose Mac computer contains mouse, keyboard and screen;
		m_ComputerBuilder->BuildMouse();
		m_ComputerBuilder->BuildKeyboard();
		m_ComputerBuilder->BuildScreen();
	}
}

Computer* ComputerDirector::GetComputer() { return m_ComputerBuilder->GetComputer(); }
