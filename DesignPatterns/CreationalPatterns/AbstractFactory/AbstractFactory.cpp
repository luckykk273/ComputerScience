#include "AbstractFactory.h"


const char* MacButton::GetName() { return "MacButton"; }
const char* WinButton::GetName() { return "WinButton"; }

const char* MacBorder::GetName() { return "MacBorder"; }
const char* WinBorder::GetName() { return "WinBorder"; }

MacButton* MacFactory::CreateButton() { return new MacButton(); }
MacBorder* MacFactory::CreateBorder() { return new MacBorder(); }

WinButton* WinFactory::CreateButton() { return new WinButton(); }
WinBorder* WinFactory::CreateBorder() { return new WinBorder(); }
