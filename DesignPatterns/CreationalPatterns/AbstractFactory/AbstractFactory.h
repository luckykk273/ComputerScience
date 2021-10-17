#pragma once


/*************************************************
 * Define the two widgets: scroll bars & windows *
 ************************************************/
class ScrollBar  // Abstract scroll bars
{
public:
	virtual const char* GetName() const = 0;
};

class PMScrollBar : public ScrollBar  // Concrete PM scroll bars
{
public:
	const char* GetName() const override;
};

class MotifScrollBar : public ScrollBar  // Concrete Motif scroll bars
{
public:
	const char* GetName() const override;
};

class Window  // Abstract window
{
public:
	virtual const char* GetName() const = 0;
};

class PMWindow : public Window  // Concrete PM window
{
public:
	const char* GetName() const override;
};

class MotifWindow : public Window  // Concrete Motif window
{
public:
	const char* GetName() const override;
};


/**********************
 * Define the factory *
 **********************/
class WidgetFactory  // Abstract widget factory
{
public:
	virtual ScrollBar* CreateScrollBar() = 0;
	virtual Window* CreateWindow() = 0;
};

class PMWidgetFactory : public WidgetFactory  // Concrete PM widget factory
{
public:
	virtual PMScrollBar* CreateScrollBar() override;
	virtual PMWindow* CreateWindow() override;
};

class MotifWidgetFactory : public WidgetFactory  // Concrete Motif widget factory
{
public:
	virtual MotifScrollBar* CreateScrollBar() override;
	virtual MotifWindow* CreateWindow() override;
};

