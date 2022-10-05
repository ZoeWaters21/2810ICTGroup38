import wx

class DateRangeGUI(wx.Frame):
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
        self.Show(True)

        Navigation = wx.BoxSizer(wx.HORIZONTAL)
        DateRangeButton = wx.Button(pnl, label="Date Range")
        OffenceCodeButton = wx.Button(pnl, label="Offence Code")
        RadarCamButton = wx.Button(pnl, label="Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label="Mobile Phones")
        CustomQueryButton = wx.Button(pnl, label="Custom Query")

        Navigation.Add(DateRangeButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        dateRangeHead = wx.StaticText(pnl, label="Show All Cases Between 2 Dates")
        rows.Add(dateRangeHead,1, wx.ALIGN_CENTER | wx.LEFT, border=25)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRange(self, event):
        wx.MessageBox("You Are Already Here")

    def OffenceCode(self, event):
        self.Hide()
        frame = OffenceCodeGUI(None, "Offence Code Query")

    def RaderCam(self, event):
        self.Hide()
        frame = RadarCameraGUI(None, "Radar/Camera Query")

    def MobilePhone(self, event):
        self.Hide()
        frame = MobilePhoneGUI(None, "Mobile Phone Query")

    def CustomQuery(self, event):
        self.Hide()
        frame = CustomQueryGUI(None, "Custom Query")

class RadarCameraGUI(wx.Frame):
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
        self.Show(True)

        Navigation = wx.BoxSizer(wx.HORIZONTAL)
        DateRangeButton = wx.Button(pnl, label="Date Range")
        OffenceCodeButton = wx.Button(pnl, label="Offence Code")
        RadarCamButton = wx.Button(pnl, label="Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label="Mobile Phones")
        CustomQueryButton = wx.Button(pnl, label="Custom Query")

        Navigation.Add(DateRangeButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        dateRangeHead = wx.StaticText(pnl, label="Camera or Radar Based Offenses")
        rows.Add(dateRangeHead,1, wx.ALIGN_CENTER | wx.LEFT, border=25)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRange(self, event):
        self.Hide()
        frame = DateRangeGUI(None, "Date Range Query")

    def OffenceCode(self, event):
        self.Hide()
        frame = OffenceCodeGUI(None, "Offence Code Query")

    def RaderCam(self, event):
        wx.MessageBox("You Are Already Here")

    def MobilePhone(self, event):
        self.Hide()
        frame = MobilePhoneGUI(None, "Mobile Phone Query")

    def CustomQuery(self, event):
        self.Hide()
        frame = CustomQueryGUI(None, "Custom Query")

class MobilePhoneGUI(wx.Frame):
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
        self.Show(True)

        Navigation = wx.BoxSizer(wx.HORIZONTAL)
        DateRangeButton = wx.Button(pnl, label="Date Range")
        OffenceCodeButton = wx.Button(pnl, label="Offence Code")
        RadarCamButton = wx.Button(pnl, label="Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label="Mobile Phones")
        CustomQueryButton = wx.Button(pnl, label="Custom Query")

        Navigation.Add(DateRangeButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        dateRangeHead = wx.StaticText(pnl, label="Trend of Mobile Usage of time")
        rows.Add(dateRangeHead,1, wx.ALIGN_CENTER | wx.LEFT, border=25)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRange(self, event):
        self.Hide()
        frame = DateRangeGUI(None, "Date Range Query")

    def OffenceCode(self, event):
        self.Hide()
        frame = OffenceCodeGUI(None, "Offence Code Query")

    def RaderCam(self, event):
        self.Hide()
        frame = RadarCameraGUI(None, "Radar/Camera Query")

    def MobilePhone(self, event):
        wx.MessageBox("You Are Already Here")

    def CustomQuery(self, event):
        self.Hide()
        frame = CustomQueryGUI(None, "Custom Query")

class CustomQueryGUI(wx.Frame):
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
        self.Show(True)

        Navigation = wx.BoxSizer(wx.HORIZONTAL)
        DateRangeButton = wx.Button(pnl, label="Date Range")
        OffenceCodeButton = wx.Button(pnl, label="Offence Code")
        RadarCamButton = wx.Button(pnl, label="Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label="Mobile Phones")
        CustomQueryButton = wx.Button(pnl, label="Custom Query")

        Navigation.Add(DateRangeButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        dateRangeHead = wx.StaticText(pnl, label="Custom Query")
        rows.Add(dateRangeHead,1, wx.ALIGN_CENTER | wx.LEFT, border=25)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRange(self, event):
        self.Hide()
        frame = DateRangeGUI(None, "Date Range Query")

    def OffenceCode(self, event):
        self.Hide()
        frame = OffenceCodeGUI(None, "Offence Code Query")

    def RaderCam(self, event):
        self.Hide()
        frame = RadarCameraGUI(None, "Radar/Camera Query")

    def MobilePhone(self, event):
        self.Hide()
        frame = MobilePhoneGUI(None, "Mobile Phone Query")

    def CustomQuery(self, event):
        wx.MessageBox("You Are Already Here")

class OffenceCodeGUI(wx.Frame):
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
        self.Show(True)

        Navigation = wx.BoxSizer(wx.HORIZONTAL)
        DateRangeButton = wx.Button(pnl, label="Date Range")
        OffenceCodeButton = wx.Button(pnl, label="Offence Code")
        RadarCamButton = wx.Button(pnl, label="Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label="Mobile Phones")
        CustomQueryButton = wx.Button(pnl, label="Custom Query")

        Navigation.Add(DateRangeButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        dateRangeHead = wx.StaticText(pnl, label="Distribution of Cases in Each Offence Code")
        rows.Add(dateRangeHead,1, wx.ALIGN_CENTER | wx.LEFT, border=25)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRange(self, event):
        self.Hide()
        frame = DateRangeGUI(None, "Date Range Query")

    def OffenceCode(self, event):
        wx.MessageBox("You Are Already Here")

    def RaderCam(self, event):
        self.Hide()
        frame = RadarCameraGUI(None, "Radar/Camera Query")

    def MobilePhone(self, event):
        self.Hide()
        frame = MobilePhoneGUI(None, "Mobile Phone Query")

    def CustomQuery(self, event):
        self.Hide()
        frame = CustomQueryGUI(None, "Custom Query")

class HomeGUI(wx.Frame):
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


        Navigation = wx.BoxSizer(wx.HORIZONTAL)
        DateRangeButton = wx.Button(pnl, label = "Date Range")
        OffenceCodeButton = wx.Button(pnl, label = "Offence Code")
        RadarCamButton = wx.Button(pnl, label = "Radar/Camera")
        MobilePhoneButton = wx.Button(pnl, label = "Mobile Phones")
        CustomQueryButton = wx.Button(pnl, label = "Custom Query")

        Navigation.Add(DateRangeButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(OffenceCodeButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(RadarCamButton, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        Navigation.Add(MobilePhoneButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        Navigation.Add(CustomQueryButton, 1, wx.ALIGN_CENTRE | wx.BOTTOM, border=5)
        rows.Add(Navigation, 1, wx.ALIGN_LEFT | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON,self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)


        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRange(self, event):
        self.Hide()
        frame = DateRangeGUI(None,"Date Range Query")

    def OffenceCode(self, event):
        self.Hide()
        frame = OffenceCodeGUI(None, "Offence Code Query")

    def RaderCam(self, event):
        self.Hide()
        frame = RadarCameraGUI(None, "Radar/Camera Query")

    def MobilePhone(self, event):
        self.Hide()
        frame = MobilePhoneGUI(None, "Mobile Phone Query")

    def CustomQuery(self, event):
        self.Hide()
        frame = CustomQueryGUI(None, "Custom Query")



app = wx.App()
frame = HomeGUI(None, "New South Wales Traffic Penalty Analysis")
app.MainLoop()