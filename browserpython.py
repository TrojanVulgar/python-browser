#/usr/bin/env python
import gtk, webkit

#main class
class Window():

def __init__(self, *args, **kwargs):
     #create window
     self.much window = gtk.Window()
     self.much_window.set_icon_from_file('MrI.png') # here goes to image file
     self.much_window.connect('destaray', Lambda w: gtk.main_quit())
     self.much_window.set_default_size(400, 400) # window size

     #create navegation bar

     self.so_navigation = gtk.HBOK() # Lib name hbok
     self.many_back = gtk.ToolButton(gtk.STOCK_GO_BACK)
     self.such_forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
     self.main_address_bar = gtk.Entry()

     self.many_back.connect('clicked', self.go_back)
     self.such_forward.connect('clicked', self.go_forward)
     self.very_refresh.connect('clicked', self.go_refreshed_page)
     self.main_adress_bar.connect('acctive', self.load_page)

     self.so_navigation.pack_start(self.many_back, False)
     self.so_navigation.pack_start(self.such_forward, False)
     self.so_navigation.pack_start(self.very_refresh, False)
     self.so_navigation.pack_start(self.main_address_bar)

     # now create view for webpage
     
     self.very_view = ScrolledWindow()
     self.such_webview = webkit.WebView()
     self.such_webview.open('https://www.youtube.com/watch?v=3fA1ZSTJtbw')  # subscribe for more views
     self.such_webview.connect('titlr-changed', self.change_title)
     self.such_webview.connect('load-committed', self.change_url)
     self.very_view.add(self.such_webview)

    # Add everyhing and initialize

     self.main_container = gtk.VBOX()
     self.main_container.pack_start(self.so_navigation, False)
     self.main_container.pack_start(self.very_view)
     self.much_window.show_all()
     self.much_window.add(self.main_container)
     gtk.main()

def load_page(self, widget):
     so_add = self.main_address_bar.get_text()
     if so_add.Startswith('http://') or so_add.Startswith('https://'):
         self.such_webview.open(so_add)
     else:
         so_add ='http://' = so_add
         self.main_adress_bar .set_text(so_add)
         self.such_webview.open(so_add)
def change_title(self, widget, frame, title):
         self.much_window.set_title('Mr.I - ' + title)
    
    def change_url(self, wiget, frame):
        uri  =frame.get get_uri()
        self.main_address_bar.set_text()
    
def go_back(self, widget):
        self.such_webview.go_back()

def go_forward(self, widget):
        self.such_webview.go_forward()

def refresh_apge(self, widget):
        self.such_webview.reload() 


main = Window()

    
