#Coffee Shop Simulator
#Wolfgang C. Stover
#02/29/2024

#Greating for Coffee Shop Simulator
print("Welcome to Wolfgang's Coffee Shop!")
 
#Constants

priceOfAmericano = 1
priceOfDonut = 1
priceOfRedBull = 2

#tax

tax = 0.06

nbrOfAmericano = int(input('Number of Americano(s) bought: '))
nbrOfDonut  = int(input('Number of donut(s) bought: '))
nbrOfRedBull = int(input('Number of Red Bull(s) bought: '))

#SubTotal Calculations

subTotalAmericano = nbrOfAmericano * priceOfAmericano
subTotalDonut  = nbrOfDonut  * priceOfDonut
subTotalRedBull = nbrOfRedBull  * priceOfRedBull

#Secondary Tax calculation for Total

totalNoTax = subTotalAmericano + subTotalDonut + subTotalRedBull
taxAmount = (totalNoTax * tax)
grandTotal = totalNoTax * tax + totalNoTax

#Receipt

print("*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*")

print("Thank you for visiting my Shop! I hope to see you again soon.")

print(str(nbrOfAmericano) + " Americano(s) @ $1 each: $ " + str(subTotalAmericano))
print(str(nbrOfDonut) + " Donut(s) @ $1 each: $ " + str(subTotalDonut))
print(str(nbrOfRedBull) + " Red Bull(s) @ $2 each: $ " + str(subTotalRedBull))

print("Tax at 6% = $" + str(taxAmount))

print("*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*")    

print("Total: $ " + str(grandTotal))


