from fpdf import FPDF

name = input("Enter name: ")

class PDF(FPDF):
    def header(self):
        width = self.w
        shirt_width = 150
        x = (width - shirt_width) / 2
        self.image("shirtificate.png", x, 100, shirt_width)
        self.set_font("Times", 'B', 24)
        self.cell(0 , 40, "CS50 Shirtificate", align='C')

pdf = PDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_y(160)
pdf.set_font("Times", "B", 12)
pdf.cell(0, 10, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")  