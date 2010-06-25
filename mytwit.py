import clr
clr.AddReference('PresentationFramework')

from System.Windows.Markup import XamlReader
from System.Windows import Application
from System.IO import FileStream, FileMode

# testing
app = Application()
app.Run(XamlReader.Load(FileStream('mytwit.xaml', FileMode.Open)))
