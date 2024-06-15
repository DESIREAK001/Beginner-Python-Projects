#importing necessary libraries
import PyPDF2
import pyttsx3

#prompt user to enter the pdf file name
pdf_filename = input("Enter the PDSF filename including the extension: ").strip()

#open the PDF file
try:
  #open the pdf file specified
  with open(pdf_filename, 'rb') as pdf_file:
    #create a pdf file reader object / read the pdf file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    #get an engine instance for the speech synthesis
    speak = pyttsx3.init()

    #iterate through each page and read the text
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      text = page.extract_text()
      if text:
        speak.say(text)
        speak.runAndWait()

    #stop the speech engine
    speak.stop()

    print("Audiobook creation completed")
except FileNotFoundError:
  print("The specified file was not found.")
except Exception as e:
  print(f"An error occured: {e}")