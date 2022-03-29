# this program takes your profit and gives you the amount of tax that you should pay yearly

array_of_tax = [2.5, 10, 15, 20, 22.5, 25]              # array of percentage that are used calculating the tax


def case_1():
    remainder = yearly_profit - 15000
    tax = 0

    for i in range(0, len(array_of_tax) + 1):

        while remainder > 0:

            if remainder >= 15000 and i < 3:

                tax += 15000 * (array_of_tax[i] / 100)
                remainder -= 15000
                i += 1

            elif i == 3 and remainder >= 140000:
                tax += 140000 * (array_of_tax[i] / 100)
                remainder -= 140000
                i += 1

            elif remainder >= 200000 and i == 4:
                tax += 200000 * (array_of_tax[i] / 100)
                remainder -= 200000
                i += 1

            else:
                tax += remainder * (array_of_tax[i] / 100)
                i += 1
                remainder = 0

    print(tax)


def case_2():
    tax = 0
    remainder = yearly_profit
    for i in range(0, len(array_of_tax) + 1):

        while remainder > 0:

            if remainder >= 15000 and i < 3:
                if i == 0:
                    tax += 30000 * (array_of_tax[i] / 100)
                    remainder -= 30000
                    i += 1

                else:
                    tax += 15000 * (array_of_tax[i] / 100)
                    remainder -= 15000
                    i += 1

            elif i == 3 and remainder >= 140000:
                tax += 140000 * (array_of_tax[i] / 100)
                remainder -= 140000
                i += 1

            elif remainder >= 200000 and i == 4:
                tax += 200000 * (array_of_tax[i] / 100)
                remainder -= 200000
                i += 1

            else:
                tax += remainder * (array_of_tax[i] / 100)
                i += 1
                remainder = 0

    print(tax)


def case_3():
    tax = 0
    remainder = yearly_profit

    for i in range(1, len(array_of_tax) + 1):

        while remainder > 0:

            if remainder >= 15000 and i < 3:
                if i == 1:
                    tax += 45000 * (array_of_tax[i] / 100)
                    remainder -= 45000
                    i += 1

                else:
                    tax += 15000 * (array_of_tax[i] / 100)
                    remainder -= 15000
                    i += 1

            elif i == 3 and remainder >= 140000:
                tax += 140000 * (array_of_tax[i] / 100)
                remainder -= 140000
                i += 1
                print(tax, i, 2)

            elif remainder >= 200000 and i == 4:
                tax += 200000 * (array_of_tax[i] / 100)
                remainder -= 200000
                i += 1

            else:
                tax += remainder * (array_of_tax[i] / 100)
                i += 1
                remainder = 0

    yearly_tax = tax
    print(yearly_tax)


def case_4():
    tax = 0
    remainder = yearly_profit

    for i in range(2, len(array_of_tax) + 1):

        while remainder > 0:

            if remainder >= 15000 and i == 2:

                tax += 60000 * (array_of_tax[i] / 100)
                remainder -= 60000
                i += 1

            elif i == 3 and remainder >= 140000:
                tax += 140000 * (array_of_tax[i] / 100)
                remainder -= 140000
                i += 1

            elif remainder >= 200000 and i == 4:
                tax += 200000 * (array_of_tax[i] / 100)
                remainder -= 200000
                i += 1

            else:
                tax += remainder * (array_of_tax[i] / 100)

                i += 1
                remainder = 0

    print(tax)


def case_5():
    tax = 0
    remainder = yearly_profit

    for i in range(3, len(array_of_tax) + 1):

        while remainder > 0:

            if remainder >= 200000 and i <= 4:
                tax += 200000 * (array_of_tax[i] / 100)
                remainder -= 200000
                i += 1

            else:
                tax += remainder * (array_of_tax[i] / 100)
                i += 1
                remainder = 0

    print(tax)


def case_6():
    tax = 0
    remainder = yearly_profit

    for i in range(4, len(array_of_tax) + 1):

        while remainder > 0:

            if remainder >= 400000 and i == 4:
                tax += 400000 * (array_of_tax[i] / 100)
                remainder -= 400000
                i += 1

            else:
                tax += remainder * (array_of_tax[i] / 100)
                i += 1
                remainder = 0

    print(tax)


def cases():
    if yearly_profit <= 15000:
        print(" this profit  is tax free")

    elif yearly_profit <= 600000:
        case_1()

    elif 700000 >= yearly_profit > 600000:
        case_2()

    elif 800000 >= yearly_profit > 700000:
        case_3()

    elif 900000 >= yearly_profit > 800000:
        case_4()

    elif 1000000 >= yearly_profit > 900000:
        case_5()

    else:
        case_6()


choice = int(input("please enter 1 to calculate for business or 2 to calculate salary tax "))
if choice == 1:
    yearly_profit = float(input("please enter the yearly profit "))
    cases()

elif choice == 2:
    monthly_salary = float(input("please enter the monthly salary "))
    yearly_profit = monthly_salary * 12
    yearly_profit -= 9000
    cases()
