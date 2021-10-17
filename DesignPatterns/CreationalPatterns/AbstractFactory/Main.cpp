#include <iostream>

#include "AbstractFactory.h"


int main()
{
	// Clients create widgets solely through the widget factory interface;
	// Clients have no knowledge of the classes that implement widgets for a particular look and feel;
	WidgetFactory* fac;  
	Window* win;
	ScrollBar* sb;
	
	// If clients want to create PM style widgets:
	fac = new PMWidgetFactory();
	win = fac->CreateWindow();
	sb = fac->CreateScrollBar();

	std::cout << "PM style widgets: " << std::endl;
	std::cout << win->GetName() << ", " << sb->GetName() << std::endl;

	// If clients want to create Motif style widgets:
	fac = new MotifWidgetFactory();
	win = fac->CreateWindow();
	sb = fac->CreateScrollBar();

	std::cout << "\nMotif style widgets: " << std::endl;
	std::cout << win->GetName() << ", " << sb->GetName() << std::endl;

	delete fac, win, sb;
}