"""
This program is designed to support peer students from COMM1180 T2, 2025
apply the key financial mathematical concepts covered in COMM1180 week 5.
The major functions are:
1. Time Value of Money (Single Cash Flow)
2. Annuity
3. Perpetuity
4. APR <=> EAR

The program is designed to be run in command line interface (CLI).

Author: Jinhao Li (z5603183), Student Partner of COMM1180 T2, 2025
"""

import math

try:
    from rich.console import Console
except ImportError:
    import sys
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
        print("Successfully installed 'rich' (a convenient console text rendering engine). Please restart the program.")
    except Exception as e:
        print(f"Failed to install 'rich': {e}")
        print("Please manually install it using: pip install rich")
    sys.exit(1)


# Constants for annuity/perpetuity types
ORDINARY_ANNUITY = "ordinary"
DUE_ANNUITY = "due"
ADVANCE_PERPETUITY = "advance"
ARREARS_PERPETUITY = "arrears"

console = Console()

def validate_type(value, cast, name):
    """
    Attempt to cast the input to desired type; raise warning on failure.
    """
    while True:
        try:
            return cast(value)
        except Exception:
            console.print(f"[bold red]Invalid input for {name}. Please enter a valid {cast.__name__}.[/]")
            value = console.input(f"{name}: ")


class TimeValueOfMoney:
    """
    Calculates future value, present value, required interest rate, and time for single cash flows.
    """
    def future_value(self, pv: float, r: float, n: int) -> float:
        return pv * (1 + r) ** n

    def present_value(self, fv: float, r: float, n: int) -> float:
        return fv / (1 + r) ** n

    def required_rate(self, pv: float, fv: float, n: int) -> float:
        return (fv / pv) ** (1 / n) - 1

    def required_time(self, pv: float, fv: float, r: float) -> float:
        return math.log(fv / pv) / math.log(1 + r)


class APRAndEAR:
    """
    Converts between Annual Percentage Rate (APR) and Effective Annual Rate (EAR).
    """
    def apr_to_ear(self, apr: float, m: int) -> float:
        return (1 + apr / m) ** m - 1

    def ear_to_apr(self, ear: float, m: int) -> float:
        return ((1 + ear) ** (1 / m) - 1) * m


class Annuity:
    """
    Handles present and future value calculations for ordinary and due annuities.
    """
    def __init__(self, r: float, n: int, C: float, ann_type: str):
        self.r, self.n, self.C, self.ann_type = r, n, C, ann_type

    def present_value(self) -> float:
        if self.ann_type == ORDINARY_ANNUITY:
            return self.C * (1 - (1 + self.r) ** -self.n) / self.r
        elif self.ann_type == DUE_ANNUITY:
            return self.C * (1 - (1 + self.r) ** -self.n) / self.r * (1 + self.r)
        else:
            raise ValueError("Invalid annuity type")

    def future_value(self) -> float:
        if self.ann_type == ORDINARY_ANNUITY:
            return self.C * ((1 + self.r) ** self.n - 1) / self.r
        elif self.ann_type == DUE_ANNUITY:
            return self.C * ((1 + self.r) ** self.n - 1) / self.r * (1 + self.r)
        else:
            raise ValueError("Invalid annuity type")


class Perpetuity:
    """
    Computes present value for perpetuities in arrears or advance.
    """
    def __init__(self, r: float, C: float, perp_type: str):
        self.r, self.C, self.perp_type = r, C, perp_type

    def present_value(self) -> float:
        if self.perp_type == ADVANCE_PERPETUITY:
            return self.C / self.r * (1 + self.r)
        elif self.perp_type == ARREARS_PERPETUITY:
            return self.C / self.r
        else:
            raise ValueError("Invalid perpetuity type")


class LearningMode:
    """
    Provides highlighted concepts and formulas in learning mode.
    """
    def time_value_of_money(self) -> str:
        return "[bold]Concept:[/] Money’s purchasing power changes over time due to interest; use PV and FV calculations to compare values across different periods."

    def future_value_single(self) -> str:
        return "[bold]Concept:[/] Growth of a single lump‑sum investment over a specified number of periods at a given interest rate.\n[bold]Formula:[/] FV = PV × (1 + r)^n"

    def present_value_single(self) -> str:
        return "[bold]Concept:[/] Determining the present value of a future amount by discounting at the appropriate rate.\n[bold]Formula:[/] PV = FV / (1 + r)^n"

    def required_rate(self) -> str:
        return "[bold]Concept:[/] Calculating the periodic interest rate needed for an initial amount to grow to a target future value over n periods.\n[bold]Formula:[/] r = (FV / PV)^(1/n) - 1"

    def required_time(self) -> str:
        return "[bold]Concept:[/] Finding the number of periods required for an investment to reach a desired future value at a given rate.\n[bold]Formula:[/] n = ln(FV / PV) / ln(1 + r)"

    def apr_and_ear(self) -> str:
        return "[bold]Concept:[/] Comparing nominal APR (stated annual rate without compounding) to the Effective Annual Rate (EAR), which reflects the true annual yield when compounding occurs m times per year.\n[bold]Formula:[/] EAR = (1 + APR/m)^m - 1; APR = ((1 + EAR)^(1/m) - 1) × m"

    def annuity_concept(self) -> str:
        return "[bold]Concept:[/] A series of equal payments made at regular intervals. An ordinary annuity has payments at the end of each period, while an annuity‑due has payments at the beginning (of each period)."

    def annuity_present(self) -> str:
        return "[bold]Formula:[/] PV = C × [1 - (1 + r)^-n] / r"

    def annuity_future(self) -> str:
        return "[bold]Formula:[/] FV = C × [(1 + r)^n - 1] / r"

    def perpetuity_concept(self) -> str:
        return "[bold]Concept:[/] A perpetuity is an infinite series of equal payments made either at the end of each period (arrears) or at the beginning (advance)."


class FinancialCalculator:
    """
    Interactive CLI for financial calculations with optional learning mode.
    """
    def __init__(self):
        self.console = console
        self.tvom = TimeValueOfMoney()
        self.conv = APRAndEAR()
        self.learning = LearningMode()
        self.learn = False

    @staticmethod
    def print_disclaimer():
        console.print("[bold red underline]DISCLAIMER: Please note that this program is not designed for professional financial advice.[/]")
        console.print("")

    def run(self):
        console.print("[bold underline green]Welcome to Financial Calculator![/]")
        console.print("")
        console.print("This program is designed to support you apply the key financial mathematical concepts covered in week 5 of COMM1180.")
        console.print("[bold blue]N.B. Where applicable, input decimal for interest rate (e.g. 0.05 for 5%).[/]")
        console.print("")
        console.print("Author: Jinhao Li (z5603183), Student Partner of COMM1180 T2, 2025")
        self.print_disclaimer()

        ans = console.input("Enable learning mode? (y/n): ").strip().lower()
        self.learn = ans in ('y', 'yes')
        print("✅") if self.learn else print("❌")

        while True:
            console.print("")
            console.print("[bold]Main Menu:[/]")
            console.print("1. Time Value of Money (Single Cash Flow)")
            console.print("2. Annuity")
            console.print("3. Perpetuity")
            console.print("4. APR <=> EAR")
            console.print("5. Exit")

            choice = console.input("Choose (1-5): ").strip()

            if choice == '1':
                self.tvm_menu()
            elif choice == '2':
                self.annuity_menu()
            elif choice == '3':
                self.perpetuity_menu()
            elif choice == '4':
                self.apr_ear_menu()
            elif choice == '5':
                console.print("Thank you for using the COMM1180 Financial Calculator!")
                self.print_disclaimer()
                break
            else:
                console.print("[bold red]Invalid choice. Please select 1-5.[/]")

    def tvm_menu(self):
        console.print("")
        console.print("[bold underline]Time Value of Money[/]")
        if self.learn:
            console.print(self.learning.time_value_of_money())

        options = {'1': 'Future Value', '2': 'Present Value', '3': 'Required Rate', '4': 'Required Time'}
        for k, v in options.items():
            console.print(f"{k}. {v}")
        choice = console.input("Select (1-4): ").strip()

        if choice == '1':
            if self.learn:
                console.print(self.learning.future_value_single())
            pv = validate_type(console.input("Enter present value (PV): "), float, 'PV')
            r = validate_type(console.input("Enter interest rate (decimal): "), float, 'rate')
            n = validate_type(console.input("Enter periods (n): "), int, 'periods')
            result = self.tvom.future_value(pv, r, n)
            console.print(f"[bold green]Future Value:[/] {result:.2f}")
        
        elif choice == '2':
            if self.learn:
                console.print(self.learning.present_value_single())
            fv = validate_type(console.input("Enter future value (FV): "), float, 'FV')
            r = validate_type(console.input("Enter interest rate (decimal): "), float, 'rate')
            n = validate_type(console.input("Enter periods (n): "), int, 'periods')
            result = self.tvom.present_value(fv, r, n)
            console.print(f"[bold green]Present Value:[/] {result:.2f}")
        
        elif choice == '3':
            if self.learn:
                console.print(self.learning.required_rate())
            pv = validate_type(console.input("Enter PV: "), float, 'PV')
            fv = validate_type(console.input("Enter FV: "), float, 'FV')
            n = validate_type(console.input("Enter periods (n): "), int, 'periods')
            result = self.tvom.required_rate(pv, fv, n)
            console.print(f"[bold green]Required Rate:[/] {result:.4f} ({result*100:.2f}%)")
        
        elif choice == '4':
            if self.learn:
                console.print(self.learning.required_time())
            pv = validate_type(console.input("Enter PV: "), float, 'PV')
            fv = validate_type(console.input("Enter FV: "), float, 'FV')
            r = validate_type(console.input("Enter rate (decimal): "), float, 'rate')
            result = self.tvom.required_time(pv, fv, r)
            console.print(f"[bold green]Required Time:[/] {result:.2f} periods")
        
        else:
            console.print("[bold red]Invalid selection (1-4).[/]")

    def annuity_menu(self):
        console.print("")
        console.print("[bold underline]Annuity Calculations[/]")
        if self.learn:
            console.print(self.learning.annuity_concept())

        rate = validate_type(console.input("Enter rate per period (decimal): "), float, 'rate')
        n = validate_type(console.input("Enter number of periods: "), int, 'periods')
        C = validate_type(console.input("Enter payment amount: "), float, 'payment')

        console.print("1. Ordinary (end)")
        console.print("2. Due (beginning)")
        typ = console.input("Select type (1-2): ").strip()
        ann_type = ORDINARY_ANNUITY if typ == '1' else DUE_ANNUITY

        console.print("1. Present Value")
        console.print("2. Future Value")
        choice = console.input("Select (1-2): ").strip()

        ann = Annuity(rate, n, C, ann_type)
        if choice == '1':
            if self.learn:
                console.print(self.learning.annuity_present())
            result = ann.present_value()
            console.print(f"[bold green]Present Value:[/] {result:.2f}")
        elif choice == '2':
            if self.learn:
                console.print(self.learning.annuity_future())
            result = ann.future_value()
            console.print(f"[bold green]Future Value:[/] {result:.2f}")
        else:
            console.print("[bold red]Invalid selection (1-2).[/]")

    def perpetuity_menu(self):
        console.print("")
        console.print("[bold underline]Perpetuity Calculations[/]")
        if self.learn:
            console.print(self.learning.perpetuity_concept())

        rate = validate_type(console.input("Enter rate (decimal): "), float, 'rate')
        C = validate_type(console.input("Enter payment amount: "), float, 'payment')
        console.print("1. Ordinary (end)")
        console.print("2. Due (beginning)")
        typ = console.input("Select type (1-2): ").strip()
        perp_type = ARREARS_PERPETUITY if typ == '1' else ADVANCE_PERPETUITY

        result = Perpetuity(rate, C, perp_type).present_value()
        console.print(f"[bold green]Present Value:[/] {result:.2f}")

    def apr_ear_menu(self):
        console.print("")
        console.print("[bold underline]APR/EAR Conversions[/]")
        if self.learn:
            console.print(self.learning.apr_and_ear())

        console.print("1. APR -> EAR")
        console.print("2. EAR -> APR")
        choice = console.input("Select (1-2): ").strip()

        if choice == '1':
            apr = validate_type(console.input("Enter APR (decimal): "), float, 'APR')
            m = validate_type(console.input("Enter compounding periods: "), int, 'periods')
            result = self.conv.apr_to_ear(apr, m)
            console.print(f"[bold green]EAR:[/] {result:.4f} ({result*100:.2f}%)")
        elif choice == '2':
            ear = validate_type(console.input("Enter EAR (decimal): "), float, 'EAR')
            m = validate_type(console.input("Enter compounding periods: "), int, 'periods')
            result = self.conv.ear_to_apr(ear, m)
            console.print(f"[bold green]APR:[/] {result:.4f} ({result*100:.2f}%)")
        else:
            console.print("[bold red]Invalid selection (1-2).[/]")


if __name__ == '__main__':
    FinancialCalculator().run()
