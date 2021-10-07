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
class AbstractButtonFactory  // Abstract button factory
{
public:
	virtual Button* CreateButton() = 0;
};

class MacButtonFactory : public AbstractButtonFactory  // Concrete mac button factory
{
public:
	MacButton* CreateButton() override;
};

class WinButtonFactory : public AbstractButtonFactory  // Concrete win button factory
{
public:
	WinButton* CreateButton() override;
};

class AbstractBorderFactory  // Abstract border factory
{
public:
	virtual Border* CreateBorder() = 0;
};

class MacBorderFactory : public AbstractBorderFactory  // Concrete mac border factory
{
public:
	MacBorder* CreateBorder() override;
};

class WinBorderFactory : public AbstractBorderFactory  // Concrete win border factory
{
public:
	WinBorder* CreateBorder() override;
};
