from enum import Enum
from datetime import date

class Color(Enum):
    WHITE = 1
    PINK = 2
    PURPLE = 3
    BLUE = 4

class Cell:
    def __init__(self, value = '', color = 'WHITE'):
        self.__value = str(value)
        color = color.upper()
        self.__color = Color[color].value
    
    def setValue(self, value : str) -> None:
        self.__value = str(value)

    def getValue(self) -> str:
        return self.__value
    
    def setColor(self, color):
        color = color.upper()
        try:
            Color[color].value
        except:
            print(f'{color} is not a valid color!')
            return -1
        else:
            self.__color = Color[color].value
            return 0

    def getColor(self) -> str:
        return Color(self.__color).name

    def toInt(self) -> int:
        try:
            int(self.__value)
        except:
            return 'CastError'
        else:
            return int(self.__value)
    
    def toDouble(self) -> float:
        try:
            float(self.__value)
        except:
            return 'CastError'
        else:
            return float(self.__value)
    
    def toDate(self) -> None:
        if len(self.__value) == 10:
            if self.__value[4] == self.__value[7] == '-':
                dateLs = self.__value.split('-')
                for i in range(len(dateLs)):
                    try:
                        int(dateLs[i])
                    except:
                        return 'CastError'
                    else:
                        dateLs[i] = int(dateLs[i])
                myDate = date(dateLs[0], dateLs[1], dateLs[2])
                return myDate
        return 'CastError'

    def reset(self) -> None:
        self.__value = ''
        self.__color = Color.WHITE.value

    def __eq__(self, other) -> bool:
        if self.getValue() == other.getValue():
            if self.getColor() == other.getColor():
                return True
        return False

class Spreadsheet:
    def __init__(self, row = 5, col = 5) -> None:
        cell = Cell()
        self.__cells = []
        for i in range(row):
            self.__cells.append([cell] * col)

    def setCellAt(self, row, col, cellOrStr) -> None:
        if (row < 1 or row > self.getRowNum()) or (col < 1 or col > self.getColNum()):
            print('Index out of range!')
            return -1
        if isinstance(cellOrStr, Cell):
            self.__cells[row -1][col -1] = cellOrStr
        if isinstance(cellOrStr, str):
            tmp = Cell(value = cellOrStr)
            self.__cells[row - 1][col - 1] = tmp

    
    def getCellAt(self, row, col) -> None:
        if (row < 1 or row > self.getRowNum()) or (col < 1 or col > self.getColNum()):
            print('Index out of range!')
            return -1
        return self.__cells[row - 1][col - 1]

    def addRow(self, row) -> None:
        if row < 1 or row > self.getRowNum():
            print('Out of range!')
            return -1
        cell = Cell()
        newRow = [cell] * len(self.__cells[0])

        first = self.__cells[:row]
        second = self.__cells[row:]

        for i in range(len(self.__cells)):
            self.__cells.pop()

        self.__cells += first
        self.__cells.append(newRow)
        self.__cells += second

    
    def removeRow(self, row) -> None:
        if row < 1 or row > self.getRowNum():
            print('Out of range!')
            return -1    
        first = self.__cells[:(row - 1)]
        second = self.__cells[row:]

        for i in range(len(self.__cells)):
            self.__cells.pop()

        self.__cells += first
        self.__cells += second

    
    def addColumn(self, column) -> None:
        if column < 1 or column > self.getColNum():
            print('Out of range!')
            return -1

        cell = Cell()            
        for row in self.__cells:
            first = row[:column]
            second = row[column:]

            for i in range(len(row)):
                row.pop()

            row += first
            row.append(cell)
            row += second

   
    def removeColumn(self, column) -> None:
        if column < 1 or column > self.getColNum():
            print('Out of range!')
            return -1

        cell = Cell()
        for row in self.__cells:
            first = row[:(column - 1)]
            second = row[column:]

            for i in range(len(row)):
                row.pop()

            row += first

            row += second

    
    def swapRows(self, row1, row2) -> None:
        if (row1 < 1 or row1 > self.getRowNum()) or (row2 < 1 or row2 > self.getRowNum()):
            print('Out of range!')
            return -1
        tmp = self.__cells[row1 - 1]
        self.__cells[row1 - 1] = self.__cells[row2 - 1]
        self.__cells[row2 - 1] = tmp
    

    def swapColumns(self, column1, column2) -> None:
        if (column1 < 1 or column1 > self.getColNum()) or (column2 < 1 or column2 > self.getColNum()):
            print('Out of range!')
            return -1    
        for row in self.__cells:
            tmp = row[column1 - 1]
            row[column1 - 1] = row[column2 - 1]
            row[column2 - 1] = tmp   
    
    
    def getRowNum(self) -> int:
        return len(self.__cells)

    def getColNum(self) -> int:
        return len(self.__cells[0])  
    
    def getRow(self, row):
        if row < 1 or row > self.getRowNum():
            print('Out of range!')
            return -1
        return self.__cells[row - 1]
    
    def getColumn(self, column) -> None:
        if column < 1 or column > self.getColNum():
            print('Out of range!')
            return -1
        colList = []
        for row in self.__cells:
            colList.append(row[column - 1])
        return colList


