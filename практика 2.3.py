
class Worker:
    def __init__(self, name, surname, rate, days, ):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
        print(self.name, self.surname, self.rate, self.days)

    def GetSalary(self, ):
        c = self.rate * self.days
        print(f"Ваша зарплата", c)


d = Worker("Адрей", "Викторович", 40, 30)
d.GetSalary()



class Worker:
    def __init__(self, name, surname, rate, days, ):
        self._name = name
        self._surname = surname
        self._rate = rate
        self._days = days
        print(self._name, self._surname, self._rate, self._days)

    def GetSalary(self, ):
        c = self._rate * self._days
        print(f"Ваша зарплата", c)

    def name1(self):
        return self._name

    def surname1(self):
        return self._surname

    def rate1(self):
        return self._rate

    def days1(self):
        return self._days


d = Worker("Адрей", "Викторович", 40, 30)
print(d.GetSalary())
print(d.days1())
print(d.surname1())
print(d.rate1())
print(d.name1())


class Calculation:
    def __init__(self, calculationLine="Имя"):
        self.calculationLine = calculationLine

    def SetCalculationLine(self, new_calculation_line):
        self.calculationLine = new_calculation_line

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):

        return self.calculationLine

    def GetLastSymbol(self):
        if self.calculationLine:
            return self.calculationLine[-1]
        else:
            return None

    def DeleteLastSymbol(self):
        if self.calculationLine:
            self.calculationLine = self.calculationLine[:-1]
        else:
            self.calculationLine = ""


a = Calculation()

print("Исходная строка:", a.GetCalculationLine())
a.SetCalculationLine("Новая строка")
print("Строка после изменения:", a.GetCalculationLine())
a.SetLastSymbolCalculationLine("!")
print("Строка после добавления символа:", a.GetCalculationLine())
last_symbol = a.GetLastSymbol()
print("Последний символ:", last_symbol)
a.DeleteLastSymbol()
print("Строка после удаления последнего символа:", a.GetCalculationLine())