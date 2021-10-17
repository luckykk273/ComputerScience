#include "AbstractFactory.h"


const char* PMWindow::GetName() const { return "PMWindow"; }
const char* MotifWindow::GetName() const { return "MotifWindow"; }

const char* PMScrollBar::GetName() const { return "PMScrollBar"; }
const char* MotifScrollBar::GetName() const { return "MotifScrollBar"; }

PMWindow* PMWidgetFactory::CreateWindow() { return new PMWindow(); }
PMScrollBar* PMWidgetFactory::CreateScrollBar() { return new PMScrollBar(); }

MotifWindow* MotifWidgetFactory::CreateWindow() { return new MotifWindow(); }
MotifScrollBar* MotifWidgetFactory::CreateScrollBar() { return new MotifScrollBar(); }
