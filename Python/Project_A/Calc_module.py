from Calc import FabonciSeries as FS
import Calc.BasicCalc as BC
import Calc.FactCalc as FC
n=int(input("Enter a limit of series: "))
a=FS.fabonici(n)
FS.display(a)
print()

div_result=BC.div(25, 3)
FC.show(div_result)
