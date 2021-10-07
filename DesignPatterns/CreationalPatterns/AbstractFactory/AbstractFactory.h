#pragma once


/********************************************
 * Define the two products: Button & Border *
 ********************************************/
class Button  // Abstract button
{
public:
	virtual const char* GetName() = 0;
};

class MacButton : public Button  // Concrete mac button
{
public:
	const char* GetName() override;
};

class WinButton : public Button  // Concrete win button
{
public:
	const char* GetName() override;
};

class Border  // Abstract border
{
public:
	virtual const char* GetName() = 0;
};

class MacBorder : public Border  // Concrete mac border
{
public:
	const char* GetName() override;
};

class WinBorder : public Border  // Concrete win border
{
public:
	const char* GetName() override;
};


/**********************
 * Define the factory *
 **********************/
class AbstractFactory  // Abstract factory
{
public:
	virtual Button* CreateButton() = 0;
	virtual Border* CreateBorder() = 0;
};

class MacFactory : public AbstractFactory  // Concrete mac factory
{
public:
	MacButton* CreateButton() override;
	MacBorder* CreateBorder() override;
};

class WinFactory : public AbstractFactory  // Concrete win factory
{
public:
	WinButton* CreateButton() override;
	WinBorder* CreateBorder() override;
};
