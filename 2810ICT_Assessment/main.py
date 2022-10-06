import wx
import pandas as pd

searchDateBefore = ""
searchDateAfter = ""
keyword = ""
keyword1 =""
keyword2 = ""


class DateRangeGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
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
        rows.Add(Navigation, 1, wx.ALIGN_CENTRE | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        dateRangeHead = wx.StaticText(pnl, label="Show All Cases Between 2 Dates")
        font = dateRangeHead.GetFont()
        font.PointSize += 5
        font = font.Bold()
        dateRangeHead.SetFont(font)
        inputHead = wx.StaticText(pnl, label="Input Dates")
        rows.Add(dateRangeHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=5)
        rows.Add(inputHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=5)

        dateSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.date1 = wx.TextCtrl(pnl)
        dateToST = wx.StaticText(pnl, label="TO")
        self.date2 = wx.TextCtrl(pnl)

        dateSizer.Add(self.date1, 1, wx.ALIGN_CENTER | wx.RIGHT)
        dateSizer.Add(dateToST, 1, wx.ALIGN_CENTER | wx.LEFT, border=50)
        dateSizer.Add(self.date2, 1, wx.ALIGN_CENTER)
        rows.Add(dateSizer, 2, wx.ALIGN_CENTER)

        beforeAfterSizer = wx.BoxSizer(wx.HORIZONTAL)
        beforeText = wx.StaticText(pnl, label="Leave Blank for all dates before to date")
        afterText = wx.StaticText(pnl, label="Leave Blank for all dates before from date")
        beforeAfterSizer.Add(beforeText, 1, wx.ALIGN_CENTER)
        beforeAfterSizer.Add(afterText, 1, wx.ALIGN_CENTER)

        rows.Add(beforeAfterSizer, 1, wx.ALIGN_CENTER)

        DateRangeSearchButton = wx.Button(pnl, label="Search")
        rows.Add(DateRangeSearchButton, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.DataRangeResults, DateRangeSearchButton)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def DataRangeResults(self, event):
        searchDateBefore = self.date1.GetValue()
        searchDateAfter = self.date2.GetValue()
        self.Hide()
        frame = DateRangeResultsGUI(None, "Data Range Query Results", searchDateBefore, searchDateAfter)


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


class DateRangeResultsGUI(wx.Frame):
    def __init__(self, parent, title, searchDateBefore, searchDateAfter):
        wx.Frame.__init__(self, parent, title=title, size=(810, 480))
        self.initialise(searchDateBefore,searchDateAfter)

    def initialise(self, searchDateBefore, searchDateAfter):
        self.pnl = wx.Panel(self)
        self.rows = wx.BoxSizer(wx.VERTICAL)
        headingSizer = wx.BoxSizer(wx.HORIZONTAL)
        ReturnButton = wx.Button(self.pnl, label="Return")
        head = wx.StaticText(self.pnl, label="New South Wales Traffic Penalty Analysis")
        font = head.GetFont()  # get the standard font
        font.PointSize += 10  # increases the size
        font = font.Bold()  # makes it bold
        head.SetFont(font)  # resets the font
        NextPageButton = wx.Button(self.pnl, label="Next Page")
        headingSizer.Add(ReturnButton, 1, wx.ALIGN_LEFT)
        headingSizer.Add(head, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)
        headingSizer.Add(NextPageButton, 1, wx.ALIGN_LEFT)
        self.rows.Add(headingSizer, 1, wx.ALIGN_CENTER)

        self.Bind(wx.EVT_BUTTON, self.ReturnHome, ReturnButton)
        self.Bind(wx.EVT_BUTTON, self.NextPage, NextPageButton)

        if searchDateBefore == "":
            searchDateBefore = "01/01/1990"

        if searchDateAfter == "":
            searchDateAfter = "12/12/2022"

        tableData = self.dateRange(searchDateBefore, searchDateAfter)
        self.tableList = tableData.values.tolist()
        tableRows = len(self.tableList)
        print(tableRows)

        text = wx.StaticText(self.pnl, label="Results: ")
        self.rows.Add(text, 1, wx.ALIGN_CENTER)

        self.table = wx.BoxSizer(wx.VERTICAL)
        count = 0
        self.index = 0

        while count < 10:
            dataLabel =wx.StaticText(self.pnl,label = str(self.tableList[self.index]))
            font = dataLabel.GetFont()
            font.PointSize += 3
            dataLabel.SetFont(font)
            self.table.Add(dataLabel, 1, wx.ALIGN_CENTRE)
            count = count + 1
            self.index = self.index + 1
        self.rows.Add(self.table, 1, wx.ALIGN_CENTER)

        self.pnl.SetSizerAndFit(self.rows)
        self.Show(True)

    def ReturnHome(self, event):
        self.Hide()
        frame = HomeGUI(None, "New South Wales Traffic Penalty Analysis")

    def NextPage(self, event):
        self.table.Clear(True)
        count = 0

        while count < 10:

            dataLabel = wx.StaticText(self.pnl, label=str(self.tableList[self.index]))
            font = dataLabel.GetFont()
            font.PointSize += 3
            dataLabel.SetFont(font)
            self.table.Add(dataLabel, 1, wx.ALIGN_CENTRE)
            count = count + 1
            self.index = self.index + 1


    def dateRange(self, beginDate, endDate):
        df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)
        df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
        df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]
        return df2


class RadarCameraGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
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
        rows.Add(Navigation, 1, wx.ALIGN_CENTRE | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        CameraRadarHead = wx.StaticText(pnl, label="Camera or Radar Based Offenses")
        font = CameraRadarHead.GetFont()
        font.PointSize += 5
        font = font.Bold()
        CameraRadarHead.SetFont(font)
        inputHead = wx.StaticText(pnl, label="Input Dates")
        rows.Add(CameraRadarHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=25)
        rows.Add(inputHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=5)

        dateSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.date1 = wx.TextCtrl(pnl)
        dateToST = wx.StaticText(pnl, label="TO")
        self.date2 = wx.TextCtrl(pnl)

        dateSizer.Add(self.date1, 1, wx.ALIGN_CENTER | wx.RIGHT)
        dateSizer.Add(dateToST, 1, wx.ALIGN_CENTER | wx.LEFT, border=50)
        dateSizer.Add(self.date2, 1, wx.ALIGN_CENTER)
        rows.Add(dateSizer, 2, wx.ALIGN_CENTER)

        beforeAfterSizer = wx.BoxSizer(wx.HORIZONTAL)
        beforeText = wx.StaticText(pnl, label="Leave Blank for all dates before to date")
        afterText = wx.StaticText(pnl, label="Leave Blank for all dates before from date")
        beforeAfterSizer.Add(beforeText, 1, wx.ALIGN_CENTER)
        beforeAfterSizer.Add(afterText, 1, wx.ALIGN_CENTER)

        rows.Add(beforeAfterSizer, 1, wx.ALIGN_CENTER)

        CameraRadarSearchButton = wx.Button(pnl, label="Search")
        rows.Add(CameraRadarSearchButton, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.RadarCameraResultsGUI, CameraRadarSearchButton)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def RadarCameraResultsGUI(self, event):
        searchDateBefore = self.date1.GetValue()
        searchDateAfter = self.date2.GetValue()
        keyword1 = "Radar"
        keyword2 = "Camera"
        self.Hide()
        frame = RadarCameraResultsGUI(None, "Radar/Camera Query Results",searchDateBefore, searchDateAfter,keyword1, keyword2)

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


class RadarCameraResultsGUI(wx.Frame):
    def __init__(self, parent, title,searchDateBefore, searchDateAfter,keyword1, keyword2):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
        self.initialise(searchDateBefore, searchDateAfter,keyword1, keyword2)

    def initialise(self,searchDateBefore, searchDateAfter,keyword1, keyword2):
        self.pnl = wx.Panel(self)
        self.rows = wx.BoxSizer(wx.VERTICAL)
        headingSizer = wx.BoxSizer(wx.HORIZONTAL)
        ReturnButton = wx.Button(self.pnl, label="Return")
        NextPageButton = wx.Button(self.pnl, label="Next Page")
        head = wx.StaticText(self.pnl, label="New South Wales Traffic Penalty Analysis")
        font = head.GetFont()  # get the standard font
        font.PointSize += 10  # increases the size
        font = font.Bold()  # makes it bold
        head.SetFont(font)  # resets the font
        headingSizer.Add(ReturnButton, 1, wx.ALIGN_LEFT)
        headingSizer.Add(head, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)
        headingSizer.Add(NextPageButton, 1, wx.ALIGN_LEFT)
        self.rows.Add(headingSizer, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.ReturnHome, ReturnButton)
        self.Bind(wx.EVT_BUTTON, self.NextPage, NextPageButton)

        if searchDateBefore == "":
            searchDateBefore = "01/01/1990"

        if searchDateAfter == "":
            searchDateAfter = "12/12/2022"

        tableData = self.customSearch(searchDateBefore, searchDateAfter, keyword1,keyword2)
        self.tableList = tableData.values.tolist()
        tableRows = len(self.tableList)
        print(tableRows)

        text = wx.StaticText(self.pnl, label="Results: ")
        self.rows.Add(text, 1, wx.ALIGN_CENTER)

        self.table = wx.BoxSizer(wx.VERTICAL)
        count = 0
        self.index = 0

        while count < 10:
            dataLabel = wx.StaticText(self.pnl, label=str(self.tableList[self.index]))
            font = dataLabel.GetFont()
            font.PointSize += 3
            dataLabel.SetFont(font)
            self.table.Add(dataLabel, 1, wx.ALIGN_CENTRE)
            count = count + 1
            self.index = self.index + 1
        self.rows.Add(self.table, 1, wx.ALIGN_CENTER)

        self.pnl.SetSizerAndFit(self.rows)
        self.Show(True)

    def ReturnHome(self, event):
        self.Hide()
        frame = HomeGUI(None, "New South Wales Traffic Penalty Analysis")

    def NextPage(self, event):
        self.table.Clear(True)
        count = 0

        while count < 10:
            dataLabel = wx.StaticText(self.pnl, label=str(self.tableList[self.index]))
            font = dataLabel.GetFont()
            font.PointSize += 3
            dataLabel.SetFont(font)
            self.table.Add(dataLabel, 1, wx.ALIGN_CENTRE)
            count = count + 1
            self.index = self.index + 1

    def customSearch(self, beginDate, endDate, keyword1, keyword2):
        df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)
        df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
        df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]

        df3 = df2[df2["OFFENCE_DESC"].str.lower().str.contains(keyword1)]
        df4 = df2[df2["OFFENCE_DESC"].str.lower().str.contains(keyword2)]

        print(type(df3))
        return df3


class MobilePhoneGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
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
        rows.Add(Navigation, 1, wx.ALIGN_CENTRE | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        MobilePhoneHead = wx.StaticText(pnl, label="Trend of Mobile Usage of time")
        font = MobilePhoneHead.GetFont()
        font.PointSize += 5
        font = font.Bold()
        MobilePhoneHead.SetFont(font)
        rows.Add(MobilePhoneHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=25)

        MobilePhoneSearchButton = wx.Button(pnl, label="Search")
        rows.Add(MobilePhoneSearchButton, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.MobilePhoneResults, MobilePhoneSearchButton)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def MobilePhoneResults(self, event):
        self.Hide()
        frame = MobilePhoneResultsGUI(None, "Mobile Phone Query Results")

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


class MobilePhoneResultsGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
        self.initialise()

    def initialise(self):
        pnl = wx.Panel(self)
        rows = wx.BoxSizer(wx.VERTICAL)
        headingSizer = wx.BoxSizer(wx.HORIZONTAL)
        ReturnButton = wx.Button(pnl, label="Return")
        head = wx.StaticText(pnl, label="New South Wales Traffic Penalty Analysis")
        font = head.GetFont()  # get the standard font
        font.PointSize += 10  # increases the size
        font = font.Bold()  # makes it bold
        head.SetFont(font)  # resets the font
        headingSizer.Add(ReturnButton, 1, wx.ALIGN_LEFT)
        headingSizer.Add(head, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)
        rows.Add(headingSizer, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.ReturnHome, ReturnButton)

        text = wx.StaticText(pnl, label="Mobile Phone Results Go Here")
        rows.Add(text, 1, wx.ALIGN_CENTER)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def ReturnHome(self, event):
        self.Hide()
        frame = HomeGUI(None, "New South Wales Traffic Penalty Analysis")


class CustomQueryGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
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
        rows.Add(Navigation, 1, wx.ALIGN_CENTRE | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        CustomQueryHead = wx.StaticText(pnl, label="Custom Query ")
        font = CustomQueryHead.GetFont()
        font.PointSize += 5
        font = font.Bold()
        CustomQueryHead.SetFont(font)
        inputHead = wx.StaticText(pnl, label="Input Dates")
        rows.Add(CustomQueryHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=5)
        rows.Add(inputHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=5)

        keywordSizer = wx.BoxSizer(wx.HORIZONTAL)
        keywordLabel = wx.StaticText(pnl, label="Keyword: ")
        self.keywordTextCtrl = wx.TextCtrl(pnl)
        keywordSizer.Add(keywordLabel, 1, wx.ALIGN_CENTER)
        keywordSizer.Add(self.keywordTextCtrl, 1, wx.ALIGN_CENTER)
        rows.Add(keywordSizer, 1, wx.ALIGN_CENTER)

        dateSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.date1 = wx.TextCtrl(pnl)
        dateToST = wx.StaticText(pnl, label="TO")
        self.date2 = wx.TextCtrl(pnl)

        dateSizer.Add(self.date1, 1, wx.ALIGN_CENTER | wx.RIGHT)
        dateSizer.Add(dateToST, 1, wx.ALIGN_CENTER | wx.LEFT, border=50)
        dateSizer.Add(self.date2, 1, wx.ALIGN_CENTER)
        rows.Add(dateSizer, 2, wx.ALIGN_CENTER)

        beforeAfterSizer = wx.BoxSizer(wx.HORIZONTAL)
        beforeText = wx.StaticText(pnl, label="Leave Blank for all dates before to date")
        afterText = wx.StaticText(pnl, label="Leave Blank for all dates before from date")
        beforeAfterSizer.Add(beforeText, 1, wx.ALIGN_CENTER)
        beforeAfterSizer.Add(afterText, 1, wx.ALIGN_CENTER)

        rows.Add(beforeAfterSizer, 1, wx.ALIGN_CENTER)

        CustomQuerySearchButton = wx.Button(pnl, label="Search")
        rows.Add(CustomQuerySearchButton, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.CustomQueryResults, CustomQuerySearchButton)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def CustomQueryResults(self, event):
        searchDateBefore = self.date1.GetValue()
        searchDateAfter = self.date2.GetValue()
        keyword = self.keywordTextCtrl.GetValue()
        self.Hide()
        frame = CustomQueryResultsGUI(None, "Custom Query Results", searchDateBefore, searchDateAfter,keyword)

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


class CustomQueryResultsGUI(wx.Frame):
    def __init__(self, parent, title, searchDateBefore, searchDateAfter,keyword):
        wx.Frame.__init__(self, parent, title=title, size=(650, 320))
        self.initialise(searchDateBefore, searchDateAfter,keyword)

    def initialise(self,searchDateBefore, searchDateAfter,keyword):
        self.pnl = wx.Panel(self)
        self.rows = wx.BoxSizer(wx.VERTICAL)
        headingSizer = wx.BoxSizer(wx.HORIZONTAL)
        ReturnButton = wx.Button(self.pnl, label="Return")
        NextPageButton = wx.Button(self.pnl, label="Next Page")
        head = wx.StaticText(self.pnl, label="New South Wales Traffic Penalty Analysis")
        font = head.GetFont()  # get the standard font
        font.PointSize += 10  # increases the size
        font = font.Bold()  # makes it bold
        head.SetFont(font)  # resets the font
        headingSizer.Add(ReturnButton, 1, wx.ALIGN_LEFT)
        headingSizer.Add(head, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)
        headingSizer.Add(NextPageButton, 1, wx.ALIGN_LEFT)
        self.rows.Add(headingSizer, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.ReturnHome, ReturnButton)
        self.Bind(wx.EVT_BUTTON, self.NextPage, NextPageButton)



        if searchDateBefore == "":
            searchDateBefore = "01/01/1990"

        if searchDateAfter == "":
            searchDateAfter = "12/12/2022"

        tableData = self.customSearch(searchDateBefore,searchDateAfter,keyword)
        self.tableList = tableData.values.tolist()
        tableRows = len(self.tableList)
        print(tableRows)

        text = wx.StaticText(self.pnl, label="Results: " )
        self.rows.Add(text, 1, wx.ALIGN_CENTER)

        self.table = wx.BoxSizer(wx.VERTICAL)
        count = 0
        self.index = 0

        while count < 10:
            dataLabel = wx.StaticText(self.pnl, label=str(self.tableList[self.index]))
            font = dataLabel.GetFont()
            font.PointSize += 3
            dataLabel.SetFont(font)
            self.table.Add(dataLabel, 1, wx.ALIGN_CENTRE)
            count = count + 1
            self.index = self.index + 1
        self.rows.Add(self.table, 1, wx.ALIGN_CENTER)

        self.pnl.SetSizerAndFit(self.rows)
        self.Show(True)

    def ReturnHome(self, event):
        self.Hide()
        frame = HomeGUI(None, "New South Wales Traffic Penalty Analysis")

    def NextPage(self, event):
        self.table.Clear(True)
        count = 0

        while count < 10:
            dataLabel = wx.StaticText(self.pnl, label=str(self.tableList[self.index]))
            font = dataLabel.GetFont()
            font.PointSize += 3
            dataLabel.SetFont(font)
            self.table.Add(dataLabel, 1, wx.ALIGN_CENTRE)
            count = count + 1
            self.index = self.index + 1

    def customSearch(self, beginDate, endDate, searchWord):
        df = pd.read_csv('penalty_data_set_2.csv', low_memory=False, parse_dates=['OFFENCE_MONTH'], dayfirst=True)
        df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])
        df2 = df[(df['OFFENCE_MONTH'] > beginDate) & (df['OFFENCE_MONTH'] < endDate)]

        df3 = df2[df2["OFFENCE_DESC"].str.lower().str.contains(searchWord)]
        return df3


class OffenceCodeGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
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
        rows.Add(Navigation, 1, wx.ALIGN_CENTRE | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

        OffenceCodeHead = wx.StaticText(pnl, label="Distribution of Cases in Each Offence Code")
        font = OffenceCodeHead.GetFont()
        font.PointSize += 5
        font = font.Bold()
        OffenceCodeHead.SetFont(font)
        inputHead = wx.StaticText(pnl, label="Input Dates")
        rows.Add(OffenceCodeHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=25)
        rows.Add(inputHead, 1, wx.ALIGN_CENTER | wx.LEFT, border=5)

        dateSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.date1 = wx.TextCtrl(pnl)
        dateToST = wx.StaticText(pnl, label="TO")
        self.date2 = wx.TextCtrl(pnl)

        dateSizer.Add(self.date1, 1, wx.ALIGN_CENTER | wx.RIGHT)
        dateSizer.Add(dateToST, 1, wx.ALIGN_CENTER | wx.LEFT, border=50)
        dateSizer.Add(self.date2, 1, wx.ALIGN_CENTER)
        rows.Add(dateSizer, 2, wx.ALIGN_CENTER)

        beforeAfterSizer = wx.BoxSizer(wx.HORIZONTAL)
        beforeText = wx.StaticText(pnl, label="Leave Blank for all dates before to date")
        afterText = wx.StaticText(pnl, label="Leave Blank for all dates before from date")
        beforeAfterSizer.Add(beforeText, 1, wx.ALIGN_CENTER)
        beforeAfterSizer.Add(afterText, 1, wx.ALIGN_CENTER)

        rows.Add(beforeAfterSizer, 1, wx.ALIGN_CENTER)

        OffenceCodeSearchButton = wx.Button(pnl, label="Search")
        rows.Add(OffenceCodeSearchButton, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.OffenceCodeResults, OffenceCodeSearchButton)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def OffenceCodeResults(self, event):
        self.Hide()
        frame = OffenceCodeResultsGUI(None, "Offence Code Query Results")

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


class OffenceCodeResultsGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
        self.initialise()

    def initialise(self):
        pnl = wx.Panel(self)
        rows = wx.BoxSizer(wx.VERTICAL)
        headingSizer = wx.BoxSizer(wx.HORIZONTAL)
        ReturnButton = wx.Button(pnl, label="Return")
        head = wx.StaticText(pnl, label="New South Wales Traffic Penalty Analysis")
        font = head.GetFont()  # get the standard font
        font.PointSize += 10  # increases the size
        font = font.Bold()  # makes it bold
        head.SetFont(font)  # resets the font
        headingSizer.Add(ReturnButton, 1, wx.ALIGN_LEFT)
        headingSizer.Add(head, 1, wx.ALIGN_CENTER | wx.BOTTOM, border=2)
        rows.Add(headingSizer, 1, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON, self.ReturnHome, ReturnButton)

        text = wx.StaticText(pnl, label="Offence Code Results Go Here")
        rows.Add(text, 1, wx.ALIGN_CENTER)

        pnl.SetSizerAndFit(rows)
        self.Show(True)

    def ReturnHome(self, event):
        self.Hide()
        frame = HomeGUI(None, "New South Wales Traffic Penalty Analysis")


class HomeGUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 320))
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
        rows.Add(Navigation, 1, wx.ALIGN_CENTRE | wx.LEFT, border=5)

        self.Bind(wx.EVT_BUTTON, self.DataRange, DateRangeButton)
        self.Bind(wx.EVT_BUTTON, self.OffenceCode, OffenceCodeButton)
        self.Bind(wx.EVT_BUTTON, self.RaderCam, RadarCamButton)
        self.Bind(wx.EVT_BUTTON, self.MobilePhone, MobilePhoneButton)
        self.Bind(wx.EVT_BUTTON, self.CustomQuery, CustomQueryButton)

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
        self.Hide()
        frame = CustomQueryGUI(None, "Custom Query")


app = wx.App()
frame = HomeGUI(None, "New South Wales Traffic Penalty Analysis")
app.MainLoop()