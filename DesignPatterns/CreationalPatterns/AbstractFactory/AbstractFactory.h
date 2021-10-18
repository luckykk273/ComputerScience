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

/******************************************
 * Define the two factories: Windows, Mac *
 ******************************************/
class PartFactory  // Abstract factory
{
public:
	virtual Mouse* CreateMouse() const = 0;
	virtual Keyboard* CreateKeyboard() const = 0;
};

class WindowsFactory : public PartFactory  // Concrete factory
{
public:
	WindowsMouse* CreateMouse() const override;
	WindowsKeyboard* CreateKeyboard() const override;
};

class MacFactory : public PartFactory  // Concrete factory
{
public:
	MacMouse* CreateMouse() const override;
	MacKeyboard* CreateKeyboard() const override;
};

