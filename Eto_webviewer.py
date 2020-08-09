import Rhino
import scriptcontext
import System
import System.Drawing as sd
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms

class SampleWebViewDialog(forms.Dialog[bool]):
    def __init__(self):
        self.Title = 'Web View Test'
        self.Padding = drawing.Padding(10)
        self.Resizable = True

        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick

        self.AbortButton = forms.Button(Text = 'Cancel')

        self.m_webview = forms.WebView()
        self.m_webview.Size = drawing.Size(900, 400)
        self.m_webview.Url = System.Uri('http://www.google.com/')

        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.BeginVertical()
        layout.AddRow(self.m_webview)
        layout.EndVertical()
        layout.AddRow(None) # spacer

        layout.BeginVertical()
        layout.AddRow(self.DefaultButton, self.AbortButton)
        layout.EndVertical()

        self.Content = layout

    def OnCloseButtonClick(self, sender, e):
        self.Close(False)

    def OnOKButtonClick(self, sender, e):
        self.Close(True)

def WebViewerExample():
    dialog = SampleWebViewDialog();
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)


if __name__ == "__main__":
    WebViewerExample()
