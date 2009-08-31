
import clr

clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')
clr.AddReference('WindowsBase')

from System.IO import File
from System.Windows.Markup import XamlReader
from System.Windows import Controls as WinControls
from System.Windows import Media as WinMedia
from System.Windows import Thickness
from System.Windows import TextWrapping
from System.Windows.Input import Key
from System.Windows.Threading import DispatcherTimer as Timer
from System import TimeSpan

from System.Windows import Application

import bg_thread


class app(Application):
    winelem = dict()

    def run(self):
        self.Run(self.mainwin)


    def __init__(self, uifile='ui.xaml'):
        self._ui_file = File.OpenRead(uifile)
        self.mainwin = XamlReader.Load(self._ui_file)
        self.ticktock = Timer()
        self.ticktock.Interval = TimeSpan(0,0,5,0,0)
        self.Waddle(self.mainwin.Content, self.winelem)

        self.client = bg_thread.MT_API(username='jmj42', password='ickysonf')

        self.mainwin.Loaded += lambda _,__: self.client.GetFriendsTimeline(
            self.status_cb)

        self.winelem['TextBox']['update_status'].KeyDown += self.post_handle
        self.winelem['TextBox']['update_status'].TextChanged += self.text_handle

        self.ticktock.Tick += lambda _,__: self.client.GetFriendsTimeline(
            self.status_cb)

        self.ticktock.Start()

    ## Stolen from http://docs.google.com/Doc?id=dd59dk39_23ckv9qkfs
    ## dumps the ui heiarchy into a dict()
    def Waddle(self, c, d):
        s = str(c.__class__)
        if str(c).find("System.Windows.Controls.")>-1 and hasattr(c,"Name") and c.Name.Length>0:
            ControlType = s[s.find("'")+1:s.rfind("'")]
            if not d.has_key(ControlType):
                d[ControlType] = {}
            d[ControlType][c.Name] = c
        if hasattr(c,"Children"):
            for cc in c.Children:
                self.Waddle(cc, d)
        elif hasattr(c,"Child"):
            self.Waddle(c.Child, d)
        elif hasattr(c,"Content"):
            self.Waddle(c.Content, d)

    def status_cb(self, bgworker, evArgs):
        bgworker.RunWorkerCompleted -= self.status_cb
        if evArgs.Cancelled or evArgs.Error:
            return

        self.winelem['StackPanel']['status_sp'].Children.Clear()
        
        for i in evArgs.Result:
            new_tb = WinControls.Border()
            new_tb.BorderBrush = WinMedia.Brushes.Black
            new_tb.BorderThickness=Thickness(5,3,3,5)
            st_box = WinControls.TextBlock()
            st_box.Text = i.text
            st_box.TextWrapping = TextWrapping.Wrap
            new_tb.Child = st_box
            self.winelem['StackPanel']['status_sp'].Children.Add(new_tb)

    def post_handle(self, control, evArgs):
        print control.Text
        print len(control.Text)
        if evArgs.Key == Key.Return:
            control.IsEnabled = False
            self.client.PostUpdate(self.post_cb,
                self.client.callargs(),
                self.client.callargs(control.Text))
            
            

    def text_handle(app, control, evArgs):
        x = len(control.Text)
        app.winelem['TextBlock']['status_line'].Text = str(x)

    def post_cb(self, bgworker, evArgs, *args, **kw):
        bgworker.RunWorkerCompleted -= self.post_cb
        print args
        print kw
        print evArgs.Error
        self.winelem['TextBox']['update_status'].IsEnabled = True
        if evArgs.Error or evArgs.Cancelled:
            return
        self.winelem['TextBox']['update_status'].Clear()
        
