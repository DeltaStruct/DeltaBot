import gspread

class spread_sheet:
    def __init__(self, fn, sn):
        self.filename = str(fn)
        self.sheetname = str(sn)
        self.gs = gspread.login(os.environ["Gmail_Address"], os.environ["Gmail_Password"])
        self.doc = self.gs.open(self.filename)
        self.sheet = self.doc.worksheet(self.sheetname)
    
    def acell(self, symbol:"string") -> "ラベル指定一点取得":
        return self.sheet.acell(symbol)
      
    def cell(self, x:"int", y:"int") -> "座標指定一点取得":
        return self.sheet.cell(int(x), int(y))
      
    def update_acell(self, symbol:"string", elem:"string, 内容") -> "ラベル指定一点更新":
        self.sheet.update_acell(symbol, str(elem))
    
    def update_cell(self, x:"int", y:"int", elem:"string, 内容") -> "座標指定一点更新":
        self.sheet.update_cell(int(x), int(y), str(elem))
        
    def range(self, symbol:"string") -> "範囲取得":
        return self.sheet.range(symbol)
    
    def update_cells(self, range_ret:"range()で返したやつ") -> "範囲更新":
        self.sheet.update_cells(range_ret)
        
