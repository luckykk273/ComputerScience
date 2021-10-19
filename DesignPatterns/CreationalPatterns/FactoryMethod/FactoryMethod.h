#pragma once

/*********************************************************
 * Define the two parts of the computer: mouse, keyboard *
 * Each part has two styles:             Windows, Mac    *
 *********************************************************/
class Mouse  // Abstract product
{
public:
	virtual const char* GetName() const = 0;
};

class WindowsMouse : public Mouse  // Concrete product
{
public:
	const char* GetName() const override;
};

class MacMouse : public Mouse  // Concrete product
{
public:
	const char* GetName() const override;
};

class Keyboard
{
public:
	virtual const char* GetName() const = 0;
};

class WindowsKeyboard : public Keyboard  // Concrete product
{
public:
	const char* GetName() const override;
};

class MacKeyboard : public Keyboard  // Concrete product
{
public:
	const char* GetName() const override;
};


/********************************************************
 * Define the four factories for each specific parts:   *
 * WindowsMouse, WindowsKeyboard, MacMouse, MacKeyboard *
 ********************************************************/
class MouseFactory  // Abstract mouse factory
{

public:
	virtual Mouse* CreateMouse() = 0;
};

class WindowsMouseFactory : public MouseFactory  // Concrete Windows mouse factory
{
public:
	WindowsMouse* CreateMouse() override;
};

class MacMouseFactory : public MouseFactory  // Concrete Mac mouse factory
{
public:
	MacMouse* CreateMouse() override;
};

class KeyboardFactory  // Abstract keyboard factory
{
public:
	virtual Keyboard* CreateKeyboard() = 0;
};

class WindowsKeyboardFactory : public KeyboardFactory  // Concrete Windows keyboard factory
{
public:
	WindowsKeyboard* CreateKeyboard() override;
};

class MacKeyboardFactory : public KeyboardFactory  // Concrete Mac keyboard factory
{
public:
	MacKeyboard* CreateKeyboard() override;
};