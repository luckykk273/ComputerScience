#include "AbstractFactory.h"


/*********************************************************
 * Define the two parts of the computer: mouse, keyboard *
 * Each part has two styles:             Windows, Mac    *
 *********************************************************/
const char* WindowsMouse::GetName() const { return "WindowsMouse"; }
const char* MacMouse::GetName() const { return "MacMouse"; }

const char* WindowsKeyboard::GetName() const { return "WindowsKeyboard"; }
const char* MacKeyboard::GetName() const { return "MacKeyboard"; }


/******************************************
 * Define the two factories: Windows, Mac *
 ******************************************/
WindowsMouse* WindowsFactory::CreateMouse() const { return new WindowsMouse();  }
WindowsKeyboard* WindowsFactory::CreateKeyboard() const { return new WindowsKeyboard(); }

MacMouse* MacFactory::CreateMouse() const { return new MacMouse();  }
MacKeyboard* MacFactory::CreateKeyboard() const { return new MacKeyboard(); }
