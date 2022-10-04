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
        font = NavHead.GetFont()  # get the standard font
        font.PointSize += 3  # increases the size
        font = font.Bold()  # makes it bold
        NavHead.SetFont(font)  # resets the font
        DateRangeButton = wx.Button(pnl, label = "Date Range")
        OffenceCodeButton = wx.Button(pnl, label = "Offence Code")
        RadarCamButton = wx.Button(pnl, label = "Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label = "Mobile Phones")
        CustomQueryButton = wx.Button(pnl, label = "Custom Query")

        Navigation.Add(NavHead,1,wx.ALIGN_CENTER| wx.BOTTOM, border=5)
        Navigation.Add(DateRangeButton,1,wx.ALIGN_LEFT| wx.BOTTOM, border=5)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_LEFT | wx.BOTTOM, border=5)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_LEFT | wx.BOTTOM, border=5)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_LEFT | wx.BOTTOM, border=5)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_LEFT | wx.BOTTOM, border=20)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT| wx.LEFT, border=25)

        self.Bind(wx.EVT_BUTTON,self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)


        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRange(self, event):
        wx.MessageBox("Data Range Query")

    def OffenceCode(self, event):
        wx.MessageBox("Offence Code Query")

    def RaderCam(self, event):
        wx.MessageBox("Radar/Camera Query")

    def MobilePhone(self, event):
        wx.MessageBox("Mobile Phone Query")

    def CustomQuery(self, event):
        wx.MessageBox("Custom Query")


app = wx.App()
frame = GameGUI(None, "New South Wales Traffic Penalty Analysis")
app.MainLoop()