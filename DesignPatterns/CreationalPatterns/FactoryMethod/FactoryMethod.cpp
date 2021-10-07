#include "../include/FactoryMethod.h"

const char* MacButton::GetName() { return "MacButton"; }
const char* WinButton::GetName() { return "WinButton"; }

const char* MacBorder::GetName() { return "MacBorder"; }
const char* WinBorder::GetName() { return "WinBorder"; }

MacButton* MacButtonFactory::CreateButton() { return new MacButton(); }
WinButton* WinButtonFactory::CreateButton() { return new WinButton(); }

MacBorder* MacBorderFactory::CreateBorder() { return new MacBorder(); }
WinBorder* WinBorderFactory::CreateBorder() { return new WinBorder(); }
