import pyttsx3
import PyPDF2
book=open("Rich Dad Poor Dad.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(book,strict=False)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
for num in range(1,pages):
    page=pdfreader.getPage(pageNumber=num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()