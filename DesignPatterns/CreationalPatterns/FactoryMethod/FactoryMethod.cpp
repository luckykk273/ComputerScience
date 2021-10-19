#include <iostream>

#include "FactoryMethod.h"


/*********************************************************
 * Define the two parts of the computer: mouse, keyboard *
 * Each part has two styles:             Windows, Mac    *
 *********************************************************/
const char* WindowsMouse::GetName() const { return "WindowsMouse"; }
const char* MacMouse::GetName() const { return "MacMouse"; }

const char* WindowsKeyboard::GetName() const { return "WindowsKeyboard"; }
const char* MacKeyboard::GetName() const { return "MacKeyboard"; }


/********************************************************
 * Define the four factories for each specific parts:   *
 * WindowsMouse, WindowsKeyboard, MacMouse, MacKeyboard *
 ********************************************************/
WindowsMouse* WindowsMouseFactory::CreateMouse() { return new WindowsMouse(); }
MacMouse* MacMouseFactory::CreateMouse() { return new MacMouse(); }

WindowsKeyboard* WindowsKeyboardFactory::CreateKeyboard() { return new WindowsKeyboard(); }
MacKeyboard* MacKeyboardFactory::CreateKeyboard() { return new MacKeyboard(); }
