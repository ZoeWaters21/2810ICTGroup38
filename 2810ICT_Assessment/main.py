import wx



class GameGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 280))
        self.initialise()

    def initialise(self):

        pnl = wx.Panel(self)
        rows = wx.BoxSizer(wx.VERTICAL)
        head = wx.StaticText(pnl, label="New South Wales Traffic Penalty Analysis")
        font = head.GetFont()  # get the standard font
        font.PointSize += 10  # increases the size
        font = font.Bold()  # makes it bold
        head.SetFont(font)  # resets the font
        rows.Add(head, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)


        Navigation = wx.BoxSizer(wx.VERTICAL)
        NavHead = wx.StaticText(pnl, label="Queries")
        DateRangeButton = wx.Button(pnl, label = "Date Range")
        OffenceCodeButton = wx.Button(pnl, label = "Offence Code")
        RadarCamButton = wx.Button(pnl, label = "Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label = "Date Range")
        CustomQueryButton = wx.Button(pnl, label = "Date Range")

        Navigation.Add(NavHead,1,wx.ALIGN_LEFT|wx.LEFT, border = 50)
        Navigation.Add(DateRangeButton,1,wx.ALIGN_LEFT|wx.LEFT, border = 50)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_LEFT | wx.LEFT, border=50)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_LEFT | wx.LEFT, border=50)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_LEFT | wx.LEFT, border=50)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_LEFT | wx.LEFT, border=50)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT)


        pnl.SetSizerAndFit(rows)
        self.Show(True)


app = wx.App()
frame = GameGUI(None, "New South Wales Traffic Penalty Analysis")
app.MainLoop()