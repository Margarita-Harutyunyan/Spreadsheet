from spreadsheet import *

#Tests for class Cell

def testCellValue(value):
    c = Cell()
    c.setValue(value)
    print(f'The result of testCellValue run with {type(value)} {value} is {c.getValue() == str(value)}')


def testCellColor(color):
    c = Cell()
    print(f'The result of testCellColor run with {color} is {c.setColor(color) == 0 or c.setColor(color) == -1}')

def testCellToInt(oCell):
    res = oCell.toInt()
    print(f'The result of testCellToInt is {isinstance(res, int) or res == "CastError"}')

def testCellToDouble(oCell):
    res = oCell.toDouble()
    print(f'The result of testCellToDouble is {isinstance(res, float) or res == "CastError"}')

def testCellToDate(oCell):
    res = oCell.toDate()
    print(f'The result of testCellToDate is {isinstance(res, date) or res == "CastError"}')

#

def testCellReset():
    c = Cell('someValue', 'pink')
    c.reset()
    print(f'The result of testCellReset is {c.getValue() == "" and c.getColor() == "WHITE"}')


#Tests for class Spreadsheet
#Spreadsheet is a 5x5 matrix by default

def testStCellAt(row, col, ob):
    st = Spreadsheet()
    st.setCellAt(row, col, ob)
    if isinstance(ob, Cell):
        print(f'The result of testStCellAt run with {type(ob)} {ob}  is {st.getCellAt(row, col) == ob or st.setCellAt(row, col, ob) == -1}')
    if isinstance(ob, str):
        tmp = Cell(value = ob)
        print(f'The result of testStCellAt run with {type(ob)} {ob}  is {st.getCellAt(row, col) == tmp or st.setCellAt(row, col, ob) == -1}')

def testStAddRow(row):
    st = Spreadsheet()
    ogLen = st.getRowNum()
    st.addRow(row)
    print(f'The result of testStAddRow run with {row} is {st.getRowNum() == ogLen + 1 or st.addRow(row) == -1}')

def testStRemoveRow(row):
    st = Spreadsheet()
    ogLen = st.getRowNum()
    st.removeRow(row)
    print(f'The result of testStRemoveRow run with {row} is {st.getRowNum() == ogLen - 1 or st.removeRow(row) == -1}')

def testStAddColumn(column):
    st = Spreadsheet()
    ogLen = st.getColNum()
    st.addColumn(column)
    print(f'The result of testStAddColumn run with {column} is {(st.getColNum() == ogLen + 1) or (st.addColumn(column) == -1)}')

def testStRemoveColumn(column):
    st = Spreadsheet()
    ogLen = st.getColNum()
    st.removeColumn(column)
    print(f'The result of testStRemoveColumn run with {column} is {(st.getColNum() == ogLen - 1) or (st.removeColumn(column) == -1)}')

def testStSwapRows(st : Spreadsheet, row1, row2):
    og1 = st.getRow(row1)
    og2 = st.getRow(row2)
    st.swapRows(row1, row2)
    print(f'The result of testStSwapRows run with {row1} and {row2} is {(og1 == st.getRow(row2) and og2 == st.getRow(row1)) or st.swapRows(row1, row2) == -1}')

def testStSwapColumns(st : Spreadsheet ,col1, col2):
    st = Spreadsheet()
    og1 = st.getColumn(col1)
    og2 = st.getColumn(col2)
    st.swapColumns(col1, col2)
    print(f'The result of testStSwapColumns run with {col1} and {col2} is {(og1 == st.getColumn(col2) and og2 == st.getColumn(col1)) or st.swapColumns(col1, col2) == -1}')


#Testing class Cell
testCellValue('Value')
testCellValue(42)

testCellColor('pink')
testCellColor('PURPLE')
testCellColor('green')

c1 = Cell('42')
c2 = Cell('notInt')

testCellToInt(c1)
testCellToInt(c2)

testCellToDouble(c1)
testCellToDouble(c2)

c3 = Cell('2023-02-10')

testCellToDate(c1)
testCellToDate(c3)

testCellReset()

#Testing class Spreadsheet

testStCellAt(2, 3, c1)
testStCellAt(3, 4, 'someValue')

testStAddRow(3)
testStAddRow(-1)
testStAddRow(6)

testStRemoveRow(3)
testStRemoveRow(-1)
testStRemoveRow(6)

testStAddColumn(3)
testStAddColumn(-1)
testStAddColumn(6)

testStRemoveColumn(3)
testStRemoveColumn(-1)
testStRemoveColumn(6)

st = Spreadsheet()
st.setCellAt(2, 3, 'hello')
st.setCellAt(3, 2, 'bye')

testStSwapRows(st, 2, 3)
testStSwapRows(st, 0, 3)
testStSwapRows(st, 3, 3)
testStSwapRows(st, 3, 6)

testStSwapColumns(st, 2, 3)
testStSwapColumns(st, 0, 3)
testStSwapColumns(st, 3, 3)
testStSwapColumns(st, 3, 6)
