#pragma once

/*******************************************************************
 * Define the three parts of the computer: mouse, keyboard, screen *
 * Each part has two styles:               Windows, Mac            *
 *******************************************************************/
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

class Screen
{
public:
	virtual const char* GetName() const = 0;
};

class WindowsScreen : public Screen  // Concrete product
{
public:
	const char* GetName() const override;
};

class MacScreen : public Screen  // Concrete product
{
public:
	const char* GetName() const override;
};

/**************************************
 * Define the final product: computer *
 **************************************/
class Computer
{
public:
	void AddMouse(Mouse* mouse);
	void AddKeyboard(Keyboard* kb);
	void AddScreen(Screen* screen);
};



/**************************************************
 * Define the two computer builders: Windows, Mac *
 **************************************************/
class ComputerBuilder  // Abstract builder
{
public:
	virtual void BuildComputer() = 0;
	virtual Computer* GetComputer() const = 0;

	// The build methods are intentionally not declared pure virtual member functions,
	// letting subclasses override only the operations they are interested in.
	virtual void BuildMouse() {}
	virtual void BuildKeyboard() {}
	virtual void BuildScreen() {}
	
};

class WindowsComputerBuilder : public ComputerBuilder  // Concrete builder
{
private:
	Computer* m_Computer;
public:
	void BuildComputer() override;
	Computer* GetComputer() const override;

	// Suppose Windows computer only contains mouse and keyboard;
	void BuildMouse() override;
	void BuildKeyboard() override;
};

class MacComputerBuilder : public ComputerBuilder  // Concrete builder
{
private:
	Computer* m_Computer;
public:
	void BuildComputer() override;
	Computer* GetComputer() const override;

	// Suppose Mac computer contains mouse, keyboard and screen;
	void BuildMouse() override;
	void BuildKeyboard() override;
	void BuildScreen() override;
};


/********************************
 * Define the computer director *
 ********************************/
class ComputerDirector
{
private:
	ComputerBuilder* m_ComputerBuilder;
public:
	ComputerDirector(ComputerBuilder* cb);
	void CreateComputer(const char* style);
	Computer* GetComputer() const;
};