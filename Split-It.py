import tkinter as tk, os, csv
from tkinter.filedialog import askopenfilename, askdirectory


# Function of the simple app
def sourceFile():
    ent_sourceFile.delete(0,tk.END)
    filePath = askopenfilename(
        filetypes=[('CSV Files', '*.csv')]
    )
    if not filePath:
        return
    ent_sourceFile.insert(0, filePath)

def outputFolder():
    ent_outputFolder.delete(0,tk.END)
    filePath = askdirectory()
    if not filePath:
        return
    ent_outputFolder.insert(0, filePath)

def submit():
    sourceFilePath = ent_sourceFile.get()
    outputFolder = ent_outputFolder.get()
    sourceFile = os.path.split(sourceFilePath)[1]
    filename = sourceFile.split('.')[0]
    linesNumber = int(ent_splitRate.get())
    encoding = ent_encoding.get()
    with open(sourceFilePath, 'r', encoding='UTF-8') as source:
        reader = csv.reader(source)
        headers = next(reader)
        currentPiece = 1
        currentLimit = linesNumber
        currentOutputFile = os.path.join(outputFolder, f'{filename}-{currentPiece}.csv')
        currentWriter = csv.writer(open(currentOutputFile, 'w', encoding=encoding))
        for i, row in enumerate(reader):
            if i + 1 > currentLimit:
                currentPiece += 1
                currentLimit = linesNumber * currentPiece
                currentOutputFile = os.path.join(outputFolder, f'{filename}-{currentPiece}.csv')
                currentWriter = csv.writer(open(currentOutputFile, 'w', encoding=encoding))
                currentWriter.writerow(headers)
            currentWriter.writerow(row)
       
# The layout of the simple app
window = tk.Tk()
window.title('Spilt It')
window.geometry('800x100')
window.resizable(0, 0)

fr_sourceFile = tk.Frame(window)
fr_outputFolder = tk.Frame(window)
fr_splitRate = tk.Frame(window)
fr_encoding = tk.Frame(window)
fr_submit = tk.Frame(window)

lbl_sourceFile = tk.Label(fr_sourceFile, text='CSV File')
lbl_outputFolder = tk.Label(fr_outputFolder, text='Output Folder')
lbl_splitRate = tk.Label(fr_splitRate, text='Line Count')
lbl_encoding = tk.Label(fr_encoding, text='Encoding')

ent_sourceFile = tk.Entry(fr_sourceFile, width=75, bd=1)
ent_outputFolder = tk.Entry(fr_outputFolder, width=71, bd=1)
ent_splitRate = tk.Entry(fr_splitRate, width=32, bd=1)
ent_encoding = tk.Entry(fr_encoding, width=32, bd=1)

btn_sourceFile = tk.Button(fr_sourceFile, text='Open', command=sourceFile)
btn_outputFolder = tk.Button(fr_outputFolder, text='Output', command=outputFolder)
btn_submit = tk.Button(fr_submit, text='submit', command=submit)

fr_sourceFile.grid(row=0, column=0, sticky='ew')
fr_outputFolder.grid(row=1, column=0, sticky='ew')
fr_splitRate.grid(row=2, column=0, sticky='w')
fr_encoding.grid(row=2, column=0, sticky='e')
fr_submit.grid(row=3, column=0, sticky='e')

lbl_sourceFile.grid(row=0, column=0, sticky='w')
lbl_outputFolder.grid(row=0, column=0, sticky='w')
lbl_splitRate.grid(row=0, column=0, sticky='w')
lbl_encoding.grid(row=0, column=0, sticky='w')

ent_sourceFile.grid(row=0, column=1)
ent_outputFolder.grid(row=0, column=1)
ent_splitRate.grid(row=0, column=1)
ent_encoding.grid(row=0, column=1)

btn_sourceFile.grid(row=0, column=2, sticky='e')
btn_outputFolder.grid(row=0, column=2, sticky='e')
btn_submit.grid(row=0, column=0, sticky='e')

window.mainloop()
