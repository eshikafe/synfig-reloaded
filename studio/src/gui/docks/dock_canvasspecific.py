#   file: docks/dock_canvasspecific.py
#	Description: Template Header
#
#	Copyright (c) 2002-2005 Robert B. Quattlebaum Jr., Adrian Bentley
#   wxSynfig: Copyright (c) 2019 Austin Aigbe
#
#	This package is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License as
#	published by the Free Software Foundation; either version 2 of
#	the License, or (at your option) any later version.
#
#	This package is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#	General Public License for more details.


#include "docks/dockable.h"
import dockable
#include <gtkmm/treeview.h>
#include "instance.h"

#namespace studio {

class CanvasView;
class Instance;

class DockCanvasSpecific(Dockable):

{
	sigc::connection canvas_delete_connection;
protected:
	virtual void init_instance_vfunc(etl::loose_handle<Instance> instance);

	virtual void init_canvas_view_vfunc(etl::loose_handle<CanvasView> canvas_view);
	virtual void changed_canvas_view_vfunc(etl::loose_handle<CanvasView> canvas_view);

private:
	void init_canvas_view(CanvasView* canvas_view);
	void init_instance(etl::handle<Instance> instance);
	void delete_instance(etl::handle<Instance> instance);
	void canvas_view_changed();
	void changed_canvas_view(etl::loose_handle<CanvasView> canvas_view) { return changed_canvas_view_vfunc(canvas_view); }
public:

	etl::loose_handle<studio::CanvasView> get_canvas_view();
	etl::loose_handle<synfigapp::CanvasInterface> get_canvas_interface();

	Dock_CanvasSpecific(const synfig::String& name,const synfig::String& local_name,Gtk::StockID stock_id_=Gtk::StockID(" "));
	virtual ~Dock_CanvasSpecific();
}; // END of Dock_CanvasSpecific

}; // END of namespace studio

