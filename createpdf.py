from fpdf import FPDF

def createpdf(students,mom):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200,10,txt='MOM: ',ln=1)
    i=2
    for x1 in mom:
        pdf.cell(200,10,txt=x1,ln=i)
        i=i+1
    pdf.add_page()
    pdf.cell(200,10,txt='Attendance List: ',ln=1)
    for x1 in students:
        pdf.cell(200,10,txt=x1,ln=i)
        i=i+1
    pdf.output("name.pdf")
