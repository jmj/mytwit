import clr

clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')

from System.IO import File
from System.Windows.Markup import XamlReader
from System.Windows import Application
from System.Windows import Controls as WinControls
from System.Windows import Media as WinMedia
from System.Windows import Thickness
from System.Windows import TextWrapping

## Hack for simplejson (imported via python-twitter)
from encodings import hex_codec
from twitter import Api as API


class get_statuses(object):
    def __init__(self, num=20):
        self.s = client.GetFriendsTimeline(count=num)
    def __iter__(self):
        for i in s:
            new_tb = WinControls.Border()
            new_tb.BorderBrush = WinMedia.Brushes.Black
            new_tb.BorderThickness=Thickness(5,3,3,5)
            st_box = WinControls.TextBlock()
            st_box.Text = i.text
            st_box.TextWrapping = TextWrapping.Wrap
            new_tb.Child = st_box
            ## Seems foolish now, but eventually this will yield
            ##  a UI element that can be splatted into a layout element
            yield new_tb
        return

def get_statuses(client, num=20):

    s = client.GetFriendsTimeline(count=num)
    for i in s:
        new_tb = WinControls.Border()
        new_tb.BorderBrush = WinMedia.Brushes.Black
        new_tb.BorderThickness=Thickness(5,3,3,5)
        st_box = WinControls.TextBlock()
        st_box.Text = i.text
        st_box.TextWrapping = TextWrapping.Wrap
        new_tb.Child = st_box
        ## Seems foolish now, but eventually this will yield
        ##  a UI element that can be splatted into a layout element
        yield new_tb
    return


## Stolen from http://docs.google.com/Doc?id=dd59dk39_23ckv9qkfs
## dumps the ui heiarchy into a dict()
def Waddle(c, d):
    s = str(c.__class__)
    if str(c).find("System.Windows.Controls.")>-1 and hasattr(c,"Name") and c.Name.Length>0:
        ControlType = s[s.find("'")+1:s.rfind("'")]
        if not d.has_key(ControlType):
            d[ControlType] = {}
        d[ControlType][c.Name] = c
    if hasattr(c,"Children"):
        for cc in c.Children:
            Waddle(cc, d)
    elif hasattr(c,"Child"):
        Waddle(c.Child, d)
    elif hasattr(c,"Content"):
        Waddle(c.Content, d)


if __name__ == '__main__':
    ui_file = File.OpenRead('ui.xaml')
    window = XamlReader.Load(ui_file)

    winelem = dict()
    Waddle(window.Content, winelem)


    # Need a new twitter client
    t_client = API(username='jmj42', password='********')
    for i in get_statuses(t_client):
        winelem['StackPanel']['status_sp'].Children.Add(i)


    Application().Run(window)


