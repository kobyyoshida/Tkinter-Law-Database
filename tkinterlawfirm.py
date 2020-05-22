from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox
from tkinter import filedialog
import csv
import os

db = mysql.connect(
    host = "34.94.100.26",
    user = "root",
    passwd = "lawfirmoc",
    database = "lawfirm"
)
cursor = db.cursor()

#These helper functions are here to display entry fields for the insert page
####################################################################################################################################################################################
def displayClients(fn,ln,addFrame):

    #Client first name entry field
    firstNameLabel = Label(addFrame, text="First Name: ")
    firstNameLabel.place(relx=.2, rely=.05)
    firstNameEntry = Entry(addFrame, width=30)
    firstNameEntry.place(relx=.32, rely=.05)

    # Client last name entry field
    lastNameLabel = Label(addFrame, text="Last Name: ")
    lastNameLabel.place(relx=.2, rely=.2)
    lastNameEntry = Entry(addFrame, width=30)
    lastNameEntry.place(relx=.32, rely=.2)

    dobText = Label(addFrame,text="DOB:")
    dobText.place(relx=.2, rely=.35)
    dobEntry = Entry(addFrame, width=30)
    dobEntry.place(relx=.32, rely=.35)

    emailText = Label(addFrame,text="Email:")
    emailText.place(relx=.2, rely=.5)
    emailEntry = Entry(addFrame, width=30)
    emailEntry.place(relx=.32, rely=.5)

    phoneText = Label(addFrame,text="Phone: ")
    phoneEntry = Entry(addFrame, width=30)
    phoneText.place(relx=.2, rely=.65)
    phoneEntry.place(relx=.32, rely=.65)

    enter = Button(addFrame, text="Enter", fg="green", command=lambda: performClientUpdate(fn,ln,firstNameEntry.get(),lastNameEntry.get(),dobEntry.get(),emailEntry.get(),phoneEntry.get()))
    enter.place(relx=.45, rely=.9)

def displayCourthouseInput(addFrame, fn, ln):

    courtLabel = Label(addFrame,text="Select Courthouse")
    courtLabel.place(relx=.2,rely=.02)
    options = ["SAC", "Orange County Superior Court", "Los Angeles Superior Court", "Riverside Superior Court","San Bernardino Superior Court","San Diego Superior Court","US District Court Central","CA Appellate Court 4th District"]
    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(addFrame,clicked, *options)
    drop.place(relx=.4, rely=.02)
    print(clicked.get())


    enter = Button(addFrame, text="Enter", fg="green", command=lambda: performCourthouseUpdate(id,fn,ln,clicked.get()))
    enter.place(relx=.45, rely=.9)

def displayGCI(addFrame):
    header = Label(addFrame, text="General Case Info")
    header.place(relx=.4,rely=.05)

    caseNameLabel = Label(addFrame,text="Case Name:")
    caseNameEntry = Entry(addFrame, width=30)
    caseNameLabel.place(relx=.2, rely=.3)
    caseNameEntry.place(relx=.32, rely=.3)

    caseDesLabel = Label(addFrame,text="Description:")
    caseDesEntry = Entry(addFrame, width=30)
    caseDesLabel.place(relx=.2, rely=.5)
    caseDesEntry.place(relx=.32, rely=.5)

    enter = Button(addFrame, text="Enter", fg="green", command=lambda: performGCIupdate(caseNameEntry.get(),caseDesEntry.get()))
    enter.place(relx=.45, rely=.9)

def displayDocuments(addFrame,fn,ln):

    pleadingLabel = Label(addFrame,text="Pleading File:")
    pleadingEntry = Entry(addFrame, width=30)
    pleadingLabel.place(relx=.2, rely=.1)
    pleadingEntry.place(relx=.32, rely=.1)

    trialLabel = Label(addFrame,text="Trail File:")
    trialEntry = Entry(addFrame, width=30)
    trialLabel.place(relx=.2, rely=.2)
    trialEntry.place(relx=.32, rely=.2)

    discoveryLabel = Label(addFrame,text="Discovery:")
    discoveryEntry = Entry(addFrame, width=30)
    discoveryLabel.place(relx=.2, rely=.3)
    discoveryEntry.place(relx=.32, rely=.3)

    documentsLabel = Label(addFrame, text="Documents:")
    documentsEntry = Entry(addFrame, width=30)
    documentsLabel.place(relx=.2, rely=.4)
    documentsEntry.place(relx=.32, rely=.4)

    mainLabel = Label(addFrame, text="Main File:")
    mainEntry = Entry(addFrame, width=30)
    mainLabel.place(relx=.2, rely=.5)
    mainEntry.place(relx=.32, rely=.5)

    correspondenceLabel = Label(addFrame, text="Correspondence:")
    correspondenceEntry = Entry(addFrame, width=30)
    correspondenceLabel.place(relx=.2, rely=.6)
    correspondenceEntry.place(relx=.32, rely=.6)

    arbitrationLabel = Label(addFrame, text="Arbitration:")
    arbitrationEntry = Entry(addFrame, width=30)
    arbitrationLabel.place(relx=.2, rely=.7)
    arbitrationEntry.place(relx=.32, rely=.7)

    privilegedLabel = Label(addFrame, text="Privileged:")
    privilegedEntry = Entry(addFrame, width=30)
    privilegedLabel.place(relx=.2, rely=.8)
    privilegedEntry.place(relx=.32, rely=.8)

    witnessesLabel = Label(addFrame, text="Witnesses:")
    witnessesEntry = Entry(addFrame, width=30)
    witnessesLabel.place(relx=.2, rely=.9)
    witnessesEntry.place(relx=.32, rely=.9)

    pfindFiles = Button(addFrame,text="Browse files",fg="blue",command=lambda : fileBrowser(addFrame,0))
    pfindFiles.place(relx=.6,rely=.1)

    tfindFiles = Button(addFrame,text="Browse files",fg="blue",command=lambda : fileBrowser(addFrame,1))
    tfindFiles.place(relx=.6,rely=.2)

    dfindFiles = Button(addFrame, text="Browse files", fg="blue", command=lambda: fileBrowser(addFrame,2))
    dfindFiles.place(relx=.6, rely=.3)

    docfindFiles = Button(addFrame, text="Browse files", fg="blue", command=lambda: fileBrowser(addFrame, 3))
    docfindFiles.place(relx=.6, rely=.4)

    mainfindFiles = Button(addFrame, text="Browse files", fg="blue", command=lambda: fileBrowser(addFrame, 4))
    mainfindFiles.place(relx=.6, rely=.5)

    corrfindFiles = Button(addFrame, text="Browse files", fg="blue", command=lambda: fileBrowser(addFrame, 5))
    corrfindFiles.place(relx=.6, rely=.6)

    arbfindFiles = Button(addFrame, text="Browse files", fg="blue", command=lambda: fileBrowser(addFrame, 6))
    arbfindFiles.place(relx=.6, rely=.7)

    privfindFiles = Button(addFrame, text="Browse files", fg="blue", command=lambda: fileBrowser(addFrame, 7))
    privfindFiles.place(relx=.6, rely=.8)

    witnessfindFiles = Button(addFrame, text="Browse files", fg="blue", command=lambda: fileBrowser(addFrame, 8))
    witnessfindFiles.place(relx=.6, rely=.9)

    enterButton = Button(addFrame, text="Enter", fg="green",command=lambda:updateDocs(fn,ln,pleadingFileAddress.cget("text"),trialFileAddress.cget("text"),discoveryFileAddress.cget("text"),documentsFileAddress.cget("text"),mainFileAddress.cget("text"),corrFileAddress.cget("text"),privilegedFileAddress.cget("text"),witnessFileAddress.cget("text"),arbitrationFileAddress.cget("text")))
    enterButton.place(relx=.45,rely=.95)

def updateDocs(fn, ln, pleading, trial, discovery, documents, main, cor, privilege, witness, arb):

    cursor.execute("SELECT ClientID FROM Clients WHERE FirstName = '%s' AND LastName = '%s'" % (fn,ln))
    i = cursor.fetchall()
    id = i[0][0]
    cursor.execute("UPDATE Documents SET Pleading = '%s', Trial = '%s', Discovery = '%s', Documents = '%s', Main = '%s', Correspondence = '%s', Privileged = '%s', Witnesses = '%s',Arbitration='%s' WHERE ClientID = '%s'" % (pleading, trial, discovery, documents, main, cor, privilege, witness, arb, id))

def displayOA(addFrame,fn,ln):

    attyLabel = Label(addFrame,text="Select Attorney")
    attyLabel.place(relx=.2,rely=.07)
    attyList = getAttorneyList()
    selection = StringVar()
    selection.set(attyList[0])
    drop = OptionMenu(addFrame,selection, *attyList)
    drop.place(relx=.4, rely=.07)
    s = selection.get().split()
    cursor.execute("SELECT AttorneyID FROM OpposingAttorneys WHERE AttorneyFirstName = '%s' AND AttorneyLastName = '%s'" % (s[0],s[1]))
    a = cursor.fetchall()
    attyid = a[0][0]

    enter = Button(addFrame, text="Enter", fg="green",command=lambda:performOAupdate(attyid,fn,ln))
    enter.place(relx=.45,rely=.9)

######################################################################################################################################################################################################

#More helper functions used throughout
######################################################################################################################################################################################################
def rollback():
    db.rollback()

def com(widget):
    db.commit()
    forget(widget)

#Returns an array of all attorneys in OpposingAttorneys table
def getAttorneyList():
    attorneys = []
    counter = 0
    cursor.execute("SELECT * FROM OpposingAttorneys")
    test = cursor.fetchall()

    for i in test:
        name = test[counter][0] + ' ' + test[counter][1]
        attorneys.append(name)
        counter+=1
    return attorneys

def generateReportScreen():
    print("Generating report")

    reportFrame = Frame(root, highlightbackground="black", highlightthickness=1)
    reportFrame.place(relwidth=.9, relheight=.9, relx=.05,rely=.03)

    fileNameLabel = Label(reportFrame,text="Enter the name of the report file")
    fileNameLabel.place(relx=.1,rely=.4)

    fileNameEntry = Entry(reportFrame,width=30)
    fileNameEntry.place(relx=.4,rely=.4)

    enter = Button(reportFrame, text="Enter", fg="green",command=lambda:generateReport(fileNameEntry.get(),reportFrame))
    enter.place(relx=.45,rely=.9)

    backButton = Button(reportFrame, text="Back", command=lambda: forget(reportFrame))
    backButton.place(relx=.1, rely=.9)



def generateReport(fileName,frame):

    fileName = fileName + ".csv"
    cursor.execute("""SELECT Clients.FirstName, Clients.LastName, Clients.dob, Clients.Address, Clients.Phone, Clients.Email, 
                    Courthouse.City, Courthouse.County, Courthouse.Courthouse, 
                    OpposingAttorneys.AttorneyFirstName, OpposingAttorneys.AttorneyLastName, OpposingAttorneys.AttorneyEmail, OpposingAttorneys.AttorneyPhone
                    FROM Clients 
                    INNER JOIN Courthouse ON Clients.CourthouseID = Courthouse.CourthouseID 
                    INNER JOIN OpposingAttorneys ON AttorneyID 
                    WHERE Clients.isDeleted = 0""")
    t = cursor.fetchall()
    print(t)

    with open(fileName, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ClientFirstName', 'ClientLastName', 'DOB', 'Address', 'Email', 'Phone', 'CourthouseCity',
                         'CourthouseCounty', 'CourthouseName', 'DateFiled', 'AttorneyFirstName', 'AttorneyLastName',
                         'AttorneyEmail', 'AttorneyPhone'])
        for row in t:
            writer.writerow(row)

    success = Label(frame,text="Report successfully generated")
    success.place(relx=.4,rely=.6)


#function for bringing something to the front of the screen
def retrieve(widget):
    widget.place_retrive()

#Function for hiding something from the screen
def forget(widget):
    widget.place_forget()

def fileBrowser(frame,fileType):
    global pleadingFileAddress
    global trialFileAddress
    global discoveryFileAddress
    global documentsFileAddress
    global mainFileAddress
    global corrFileAddress
    global arbitrationFileAddress
    global privilegedFileAddress
    global witnessFileAddress

    frame.filename = filedialog.askopenfilename(initialdir="\Koby\OneDrive\Documents\DatabaseFileExample",title="Select A File")

    #testLabel.text = frame.filename
    if fileType == 0:
        pleadingFileAddress = Label(frame, text=frame.filename)
        pleadingFileAddress.place(relx=.5,rely=.37)
    elif fileType == 1:
        trialFileAddress = Label(frame, text=frame.filename)
        trialFileAddress.place(relx=.5,rely=.42)
    elif fileType == 2:
        discoveryFileAddress = Label(frame, text=frame.filename)
        discoveryFileAddress.place(relx=.5,rely=.47)
    elif fileType == 3:
        documentsFileAddress = Label(frame,text=frame.filename)
        documentsFileAddress.place(relx=.5,rely=.52)
    elif fileType == 4:
        mainFileAddress = Label(frame,text=frame.filename)
        mainFileAddress.place(relx=.5,rely=.57)
    elif fileType == 5:
        corrFileAddress = Label(frame,text=frame.filename)
        corrFileAddress.place(relx=.5,rely=.62)
    elif fileType == 6:
        arbitrationFileAddress = Label(frame,text=frame.filename)
        arbitrationFileAddress.place(relx=.5,rely=.67)
    elif fileType == 7:
        privilegedFileAddress = Label(frame,text=frame.filename)
        privilegedFileAddress.place(relx=.5,rely=.72)
    elif fileType == 8:
        witnessFileAddress = Label(frame,text=frame.filename)
        witnessFileAddress.place(relx=.5,rely=.77)

def searchPageBackButton(widget1,widget2):
    forget(widget1)
    forget(widget2)

def insertNewAtty(fn,ln,email,phone):
    cursor.execute('INSERT INTO OpposingAttorneys(AttorneyFirstName,AttorneyLastName,AttorneyEmail,AttorneyPhone) VALUES (%s,%s,%s,%s)', (fn,ln,email,phone))
    print("Insert complete")

#Function for SQL Insert query for Clients/GenCaseInfo
def performInsert(fn,ln,dob,email,phone,casename,caseDescription,courtid,attyid,pleadingFileAddress,trialFileAddress,discoveryFileAddress):

    cursor.execute('INSERT INTO Clients (FirstName,LastName,dob,Phone,Email,CourthouseID,OpposingAttorneyID) VALUES (%s,%s,%s,%s,%s,%s,%s)',(fn,ln,dob,email,phone,courtid,attyid))
    clientID = cursor.lastrowid
    cursor.execute('INSERT INTO GeneralCaseInfo (CaseName,Description,ClientID) VALUES (%s,%s,%s)',(casename,caseDescription,clientID))
    cursor.execute('INSERT INTO Documents (Pleading,Trial,Discovery,ClientID) VALUES (%s,%s,%s,%s)',(pleadingFileAddress,trialFileAddress,discoveryFileAddress,clientID))
######################################################################################################################################################################################################################

#Screens
######################################################################################################################################################################################################################
def searchPage():

    searchFrame = Frame(root, highlightbackground="black", highlightthickness=1)
    searchFrame.place(relwidth=.9, relheight=.4, relx=.05,rely=.03)

    resultFrame = Frame(root, highlightbackground="black", highlightthickness=1)
    resultFrame.place(relwidth=.9, relheight=.5,relx=.05,rely=.45)

    header = Label(searchFrame,text="Search for client:")
    header.place(relx=.4,rely=.1)

    # Client first name entry field
    firstNameLabel = Label(searchFrame, text="First Name: ")
    firstNameLabel.place(relx=.2, rely=.3)
    firstNameEntry = Entry(searchFrame, width=30)
    firstNameEntry.place(relx=.32, rely=.3)

    # Client last name entry field
    lastNameLabel = Label(searchFrame, text="Last Name: ")
    lastNameLabel.place(relx=.2, rely=.4)
    lastNameEntry = Entry(searchFrame, width=30)
    lastNameEntry.place(relx=.32, rely=.4)

    enter = Button(searchFrame, text="Enter", fg="green",command=lambda : searchIt(firstNameEntry.get(),lastNameEntry.get(),resultFrame))
    enter.place(relx=.45,rely=.85)

    backButton = Button(searchFrame, text="Back", command=lambda: searchPageBackButton(searchFrame,resultFrame))
    backButton.place(relx=.1, rely=.85)

    allInfoButton = Button(searchFrame, text="Show all info", fg="green", )

    #Display amount of records in the DB
    cursor.execute("SELECT COUNT(FirstName) FROM Clients WHERE isDeleted = 0")
    totalRecords = cursor.fetchall()
    line = "Total records in database: ", totalRecords
    totalRecordsLabel = Label(searchFrame, text=line)
    totalRecordsLabel.place(relx=.7, rely=.85)

def updateSelectionScreen(fn,ln):

    addFrame = Frame(root, highlightbackground="black", highlightthickness=1)
    addFrame.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

    cursor.execute("SELECT ClientID FROM Clients WHERE FirstName = '%s' AND LastName = '%s'" % (fn,ln))
    id = cursor.fetchall()

    options = ["Clients", "General Case Info", "Documents", "Courthouse", "Opposing Attorney"]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(addFrame,clicked, *options)
    drop.place(relx=.44, rely=.05)

    apply=Button(addFrame,text="Apply Filter",command=lambda : clickedDropDown(addFrame,clicked,fn,ln))
    apply.place(relx=.45,rely=.1)
    backButton = Button(addFrame, text="Back", command=lambda: forget(addFrame))
    backButton.place(relx=.1, rely=.9)
    saveReturnButton = Button(addFrame, text="Save & Return", command=lambda : com(addFrame))
    saveReturnButton.place(relx=.8,rely=.9)

def insertScreen():
    newnew = Frame(root, highlightbackground="black", highlightthickness=1)
    newnew.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

    #Buttons
    saveReturnButton = Button(newnew, text="Save & Return", command=lambda : com(newnew))
    saveReturnButton.place(relx=.8,rely=.95)

    undoButton = Button(newnew, text="Undo Changes",command=rollback)
    undoButton.place(relx=.1,rely=.95)

    backButton = Button(newnew, text="Back", command=lambda:forget(newnew))
    backButton.place(relx=.02, rely=.95)

    enterButton = Button(newnew, text="Enter", fg="green",command=lambda:performInsert(firstNameEntry.get(),lastNameEntry.get(),dobEntry.get(),emailEntry.get(),phoneEntry.get(),caseNameEntry.get(),caseDesEntry.get(),id,attyid,pleadingFileAddress.cget("text"),trialFileAddress.cget("text"),discoveryFileAddress.cget("text")))
    enterButton.place(relx=.45,rely=.95)

    # Client first name entry field
    firstNameLabel = Label(newnew, text="First Name: ")
    firstNameLabel.place(relx=.2, rely=.13)
    firstNameEntry = Entry(newnew, width=30)
    firstNameEntry.place(relx=.32, rely=.12)

    # Client last name entry field
    lastNameLabel = Label(newnew, text="Last Name: ")
    lastNameLabel.place(relx=.2, rely=.16)
    lastNameEntry = Entry(newnew, width=30)
    lastNameEntry.place(relx=.32, rely=.16)

    dobText = Label(newnew, text="DOB:")
    dobText.place(relx=.2, rely=.19)
    dobEntry = Entry(newnew, width=30)
    dobEntry.place(relx=.32, rely=.19)

    emailText = Label(newnew, text="Email:")
    emailText.place(relx=.2, rely=.22)
    emailEntry = Entry(newnew, width=30)
    emailEntry.place(relx=.32, rely=.22)

    phoneText = Label(newnew, text="Phone: ")
    phoneEntry = Entry(newnew, width=30)
    phoneText.place(relx=.2, rely=.25)
    phoneEntry.place(relx=.32, rely=.25)

    # Courthouse information
    courtLabel = Label(newnew,text="Select Courthouse")
    courtLabel.place(relx=.2,rely=.02)
    options = ["SAC", "OCC", "OCSC", "LASC","RSC","SBSC","SDSC","USDC-C","Cal.App.4th"]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(newnew,clicked.get(), *options)
    drop.place(relx=.4, rely=.02)
    cursor.execute("SELECT CourthouseID FROM Courthouse WHERE Courthouse = '%s'" % (clicked.get()))
    i = cursor.fetchall()
    id=i[0][0]

    addressLabel = Label(newnew, text="Address:")
    addressEntry = Entry(newnew, width=30)
    addressLabel.place(relx=.2, rely=.28)
    addressEntry.place(relx=.32, rely=.28)

    # GenCaseInfo
    caseNameLabel = Label(newnew, text="Case Name:")
    caseNameEntry = Entry(newnew, width=30)
    caseNameLabel.place(relx=.2, rely=.31)
    caseNameEntry.place(relx=.32, rely=.31)

    caseDesLabel = Label(newnew, text="Description:")
    caseDesEntry = Entry(newnew, width=30)
    caseDesLabel.place(relx=.2, rely=.34)
    caseDesEntry.place(relx=.32, rely=.34)

    dateFiledLabel = Label(newnew, text="Date Filed:")
    dateFiledEntry = Entry(newnew, width=30)
    dateFiledLabel.place(relx=.2, rely=.37)
    dateFiledEntry.place(relx=.32, rely=.37)

    # OpposingAttorneyInfo
    attyLabel = Label(newnew,text="Select Attorney")
    attyLabel.place(relx=.2,rely=.07)
    attyList = getAttorneyList()
    selection = StringVar()
    selection.set(attyList[0])
    drop = OptionMenu(newnew,selection, *attyList)
    drop.place(relx=.4, rely=.07)
    s = selection.get().split()
    cursor.execute("SELECT AttorneyID FROM OpposingAttorneys WHERE AttorneyFirstName = '%s' AND AttorneyLastName = '%s'" % (s[0],s[1]))
    a = cursor.fetchall()
    attyid = a[0][0]

    addNewAttorney = Button(newnew,text="+",command=addAttorney)
    addNewAttorney.place(relx=.53,rely=.07)

    # Documents
    pleadingLabel = Label(newnew, text="Pleading File:")
    pleadingEntry = Entry(newnew, width=30)
    pleadingLabel.place(relx=.2, rely=.42)
    pleadingEntry.place(relx=.32, rely=.42)

    trialLabel = Label(newnew, text="Trail File:")
    trialEntry = Entry(newnew, width=30)
    trialLabel.place(relx=.2, rely=.47)
    trialEntry.place(relx=.32, rely=.47)

    discoveryLabel = Label(newnew, text="Discovery:")
    discoveryEntry = Entry(newnew, width=30)
    discoveryLabel.place(relx=.2, rely=.52)
    discoveryEntry.place(relx=.32, rely=.52)

    documentsLabel = Label(newnew, text="Documents:")
    documentsEntry = Entry(newnew, width=30)
    documentsLabel.place(relx=.2, rely=.57)
    documentsEntry.place(relx=.32, rely=.57)

    mainLabel = Label(newnew, text="Main File:")
    mainEntry = Entry(newnew, width=30)
    mainLabel.place(relx=.2, rely=.62)
    mainEntry.place(relx=.32, rely=.62)

    correspondenceLabel = Label(newnew, text="Correspondence:")
    correspondenceEntry = Entry(newnew, width=30)
    correspondenceLabel.place(relx=.2, rely=.67)
    correspondenceEntry.place(relx=.32, rely=.67)

    arbitrationLabel = Label(newnew, text="Arbitration:")
    arbitrationEntry = Entry(newnew, width=30)
    arbitrationLabel.place(relx=.2, rely=.72)
    arbitrationEntry.place(relx=.32, rely=.72)

    privilegedLabel = Label(newnew, text="Privileged:")
    privilegedEntry = Entry(newnew, width=30)
    privilegedLabel.place(relx=.2, rely=.77)
    privilegedEntry.place(relx=.32, rely=.77)

    privilegedLabel = Label(newnew, text="Witnesses:")
    privilegedEntry = Entry(newnew, width=30)
    privilegedLabel.place(relx=.2, rely=.82)
    privilegedEntry.place(relx=.32, rely=.82)




    pfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,0))
    pfindFiles.place(relx=.53, rely=.42)

    tfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,1))
    tfindFiles.place(relx=.53, rely=.47)

    dfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,2))
    dfindFiles.place(relx=.53, rely=.52)

    docfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,3))
    docfindFiles.place(relx=.53, rely=.57)

    mainfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,4))
    mainfindFiles.place(relx=.53, rely=.62)

    corrfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,5))
    corrfindFiles.place(relx=.53, rely=.67)

    arbfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,6))
    arbfindFiles.place(relx=.53, rely=.72)

    privfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,7))
    privfindFiles.place(relx=.53, rely=.77)

    witnessfindFiles = Button(newnew, text="Browse files", fg="blue", command=lambda: fileBrowser(newnew,8))
    witnessfindFiles.place(relx=.53, rely=.82)

#Page for when the + button is pressed on add screen
def addAttorney():
    newAtty = Frame(highlightbackground="black", highlightthickness=1)
    newAtty.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

    header = Label(newAtty, text="Create a new attorney record")
    header.place(relx=.3,rely=.05)

    # Attorney first name entry field
    attyfirstNameLabel = Label(newAtty, text="First Name: ")
    attyfirstNameLabel.place(relx=.2, rely=.2)
    attyfirstNameEntry = Entry(newAtty, width=30)
    attyfirstNameEntry.place(relx=.32, rely=.2)

    # Attorney last name entry field
    attylastNameLabel = Label(newAtty, text="Last Name: ")
    attylastNameLabel.place(relx=.2, rely=.25)
    attylastNameEntry = Entry(newAtty, width=30)
    attylastNameEntry.place(relx=.32, rely=.25)

    #New Attorney Email
    attyemailText = Label(newAtty, text="Email:")
    attyemailText.place(relx=.2, rely=.3)
    attyemailEntry = Entry(newAtty, width=30)
    attyemailEntry.place(relx=.32, rely=.3)

    #New attorney phone number
    attyphoneText = Label(newAtty, text="Phone: ")
    attyphoneEntry = Entry(newAtty, width=30)
    attyphoneText.place(relx=.2, rely=.35)
    attyphoneEntry.place(relx=.32, rely=.35)

    #Buttons
    undoButton = Button(newAtty, text="Undo Changes",command=rollback)
    undoButton.place(relx=.1,rely=.95)

    backButton = Button(newAtty, text="Back", command=lambda:forget(newAtty))
    backButton.place(relx=.02, rely=.95)

    enterButton = Button(newAtty, text="Enter", fg="green",command=lambda:insertNewAtty(attyfirstNameEntry.get(),attylastNameEntry.get(),attyemailEntry.get(),attyphoneEntry.get()))
    enterButton.place(relx=.45,rely=.95)

    saveReturnButton = Button(newAtty, text="Save & Return", command=lambda : com(newAtty))
    saveReturnButton.place(relx=.8,rely=.95)


#So far only deletes a client
def deleteScreen():

    deleteFrame = Frame(root, highlightbackground="black", highlightthickness=1)
    deleteFrame.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

    # Client first name entry field
    firstNameLabel = Label(deleteFrame, text="First Name: ")
    firstNameEntry = Entry(deleteFrame, width=30)
    firstNameLabel.place(relx=.2, rely=.1)
    firstNameEntry.place(relx=.32, rely=.1)

    # Client last name entry field
    lastNameLabel = Label(deleteFrame, text="Last Name: ")
    lastNameEntry = Entry(deleteFrame, width=30)
    lastNameLabel.place(relx=.2, rely=.2)
    lastNameEntry.place(relx=.32, rely=.2)

    deleteButton = Button(deleteFrame,text="Delete",fg="red",command=lambda : areYouSure(deleteFrame,firstNameEntry.get(),lastNameEntry.get()))
    deleteButton.place(relx=.32,rely=.3)

    backButton = Button(deleteFrame, text="Back", command=lambda: forget(deleteFrame))
    backButton.place(relx=.1, rely=.8)

    undoButton = Button(deleteFrame, text="Undo Changes",command=rollback)
    undoButton.place(relx=.2,rely=.8)

    saveReturnButton = Button(deleteFrame, text="Save & Return", command=lambda : com(deleteFrame))
    saveReturnButton.place(relx=.8,rely=.8)

#When update button is pressed, this frame prompts user to enter which client the updates will be applied to
def updateDecide():
    who = Frame(root, highlightbackground="black", highlightthickness=1)
    who.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

    person = Label(who,text="Enter the name of the person you want to update. ")
    person.place(relx=.3, rely=.05)

    # Client first name entry field
    firstNameLabel = Label(who, text="First Name: ")
    firstNameEntry = Entry(who, width=30)
    firstNameLabel.place(relx=.2, rely=.15)
    firstNameEntry.place(relx=.32, rely=.15)

    # Client last name entry field
    lastNameLabel = Label(who, text="Last Name: ")
    lastNameEntry = Entry(who, width=30)
    lastNameLabel.place(relx=.2, rely=.2)
    lastNameEntry.place(relx=.32, rely=.2)

    enterButton = Button(who, text="Enter", fg="green",command=lambda:updateSelectionScreen(firstNameEntry.get(),lastNameEntry.get()))
    enterButton.place(relx=.5,rely=.8)

    backButton = Button(who, text="Back",command=lambda : forget(who))
    backButton.place(relx=.1,rely=.8)

######################################################################################################################################################################################################################

#This function is ran when the enter button is pressed on the search page
def searchIt(fn,ln,resultFrame):
    global query_result

    cursor.execute("SELECT * FROM Clients WHERE FirstName = '%s' AND LastName = '%s' AND isDeleted = 0" % (fn,ln))
    result = cursor.fetchall()
    id = cursor.lastrowid
    print(id)

    answer = str(result[0][0]) + " " + str(result [0][1] + "\nDOB: " + str(result[0][2]) + " Address: " + str(result[0][3]) + " Phone: " + str(result[0][4]) + " Email: " + str(result[0][5]))
    query_result = Label(resultFrame,text=answer)
    query_result.place(relx=.1,rely=.05)

    moreResults = Button(resultFrame, text="Display more results", fg="green",command=lambda : displayMoreResults(fn,ln,resultFrame))
    moreResults.place(relx=.7,rely=.8)

    findFiles = Button(resultFrame,text="Find files",command=lambda : getFiles(fn,ln,resultFrame))
    findFiles.place(relx=.45,rely=.8)

    attyContactInfoButton = Button(resultFrame,text="Get Attorney Contact Info",command=lambda : getAttyContactInfo(fn,ln,resultFrame))
    attyContactInfoButton.place(relx=.2,rely=.8)

def getAttyContactInfo(fn,ln,resultFrame):
    cursor.execute("SELECT ClientID FROM Clients WHERE FirstName = '%s' AND LastName = '%s'" % (fn,ln))
    t = cursor.fetchall()
    id = t[0][0]

    cursor.execute("SELECT OpposingAttorneys.AttorneyPhone, OpposingAttorneys.AttorneyEmail FROM OpposingAttorneys WHERE OpposingAttorneys.AttorneyID IN (SELECT AttorneyID FROM Clients WHERE Clients.ClientID = '%s')" % (id,))
    result = cursor.fetchall()

    phone = result[0][0]
    email = result[0][1]

    contactInfo = "Attorney Phone Number: ", phone, "\nAttorney Email: ", email

    attorneyContactInfo = Label(resultFrame,text=contactInfo)
    attorneyContactInfo.place(relx=.25,rely=.12)

def getFiles(fn,ln,frame):

    cursor.execute("SELECT ClientID FROM Clients WHERE FirstName = '%s' AND LastName = '%s'" % (fn,ln))
    i = cursor.fetchall()
    id = i[0][0]

    cursor.execute("SELECT * FROM Documents WHERE ClientID = '%s'" % (id,))
    t = cursor.fetchall()
    print(t)
    if t == "None":
        print("No files found.")
        return

    discoveryFile = t[0][0]
    pleadingFile = t[0][1]
    documentsFile = t[0][2]
    trialFile = t[0][3]
    mainFile = t[0][4]
    corrFile = t[0][5]
    arbitrationFile = t[0][6]
    privilegedFile = t[0][7]
    witnessesFile = t[0][8]

    ple = "Pleading file: ", pleadingFile
    dis = "Discovery file: ", discoveryFile
    doc = "Documents file: ", documentsFile
    t = "Trial file: ", trialFile
    m = "Main file: ", mainFile
    c = "Correspondence: ", corrFile
    a = "Arbitration file: ", arbitrationFile
    priv = "Privileged file: ", privilegedFile
    wit = "Witness File: ", witnessesFile


    pleading = Label(frame, text=ple, fg="blue", underline=1)
    pleading.bind("<Button-1>", lambda e: hyperlink(pleadingFile))
    pleading.place(relx=.2,rely=.2)

    discovery = Label(frame, text=dis, fg="blue", underline=1)
    discovery.bind("<Button-1>", lambda e: hyperlink(discoveryFile))
    discovery.place(relx=.2, rely=.25)

    documents = Label(frame, text=doc, fg="blue", underline=1)
    documents.bind("<Button-1>", lambda e: hyperlink(documentsFile))
    documents.place(relx=.2,rely=.3)

    trial = Label(frame, text=t, fg="blue", underline=1)
    trial.bind("<Button-1>", lambda e: hyperlink(trialFile))
    trial.place(relx=.2,rely=.35)

    main = Label(frame, text=m, fg="blue", underline=1)
    main.bind("<Button-1>", lambda e: hyperlink(mainFile))
    main.place(relx=.2,rely=.4)

    correspondence = Label(frame, text=c, fg="blue", underline=1)
    correspondence.bind("<Button-1>", lambda e: hyperlink(corrFile))
    correspondence.place(relx=.2,rely=.45)

    arbitration = Label(frame, text=a, fg="blue", underline=1)
    arbitration.bind("<Button-1>", lambda e: hyperlink(arbitrationFile))
    arbitration.place(relx=.2,rely=.5)

    privilege = Label(frame, text=ple, fg="blue", underline=1)
    privilege.bind("<Button-1>", lambda e: hyperlink(privilegedFile))
    privilege.place(relx=.2,rely=.55)

    witness = Label(frame, text=ple, fg="blue", underline=1)
    witness.bind("<Button-1>", lambda e: hyperlink(witnessesFile))
    witness.place(relx=.2,rely=.6)

def hyperlink(str):
    os.system(str)
#Button that will be used for displaying additional information after a search has been entered
def displayMoreResults(fn,ln,frame):
    print("More results")
    cursor.execute("""SELECT Clients.FirstName, Clients.LastName, Clients.dob, Clients.Address, Clients.Phone, Clients.Email, 
                    Courthouse.City, Courthouse.County, Courthouse.Courthouse,
                    OpposingAttorneys.AttorneyFirstName, OpposingAttorneys.AttorneyLastName, OpposingAttorneys.AttorneyEmail, OpposingAttorneys.AttorneyPhone
                    FROM Clients 
                    INNER JOIN Courthouse ON Clients.CourthouseID = Courthouse.CourthouseID 
                    INNER JOIN OpposingAttorneys ON AttorneyID 
                    WHERE Clients.FirstName = '%s' AND Clients.LastName = '%s'""" % (fn,ln))
    t = cursor.fetchall()
    result = str(t[0][0],t[0][1]), " Courthouse: ", str(t[0][8]), "Attorney: ", str(t[0][9],t[0][10])
    print(result)
    query_result.configure(text=result)


#This function gets called when the drop down menu is applied in the Update Screen
def clickedDropDown(addFrame,clicked,fn,ln):
    newFrame = Frame(root,highlightbackground="black", highlightthickness=1)
    newFrame.place(relwidth=.7, relheight=.5, relx=.15, rely=.2)
    backButton = Button(newFrame, text="Back", command=lambda: forget(newFrame))
    backButton.place(relx=.1, rely=.8)

    if clicked.get() == "Clients":
        displayClients(fn,ln,newFrame)
    if clicked.get() == "Courthouse":
        displayCourthouseInput(newFrame, fn, ln)
    if clicked.get() == "General Case Info":
        print("Gen case info")
        displayGCI(newFrame)
    if clicked.get() == "Documents":
        print("Documents")
        displayDocuments(newFrame,fn,ln)
    if clicked.get() == "Opposing Attorney":
        print("Opposing Attorney")
        displayOA(newFrame,fn,ln)

#When a record is deleted, this dialog box will appear
def areYouSure(deleteFrame,fn,ln):

    response = messagebox.askokcancel("Delete Record","Are you sure you want to delete this record?")
    #Label(deleteFrame, text=response).place(relx=.4, rely=.4)
    if response == 1:
        #cursor.execute("SELECT * FROM Clients WHERE FirstName = '%s' AND LastName = '%s'",(fn,ln))
        cursor.execute("UPDATE Clients SET isDeleted = True WHERE FirstName = '%s' AND LastName = '%s'" % (fn,ln))
        success = Label(deleteFrame, text="Record deleted successfully. ")
        success.place(relx=.4, rely=.4)

#Actual inserts to different tables with different parameters depending on drop down menus selected on the update page
######################################################################################################################################################################################################################
def performClientUpdate(ogfn, ogln, fn,ln,dob,email,phone):

    cursor.execute("SELECT ClientID FROM Clients WHERE FirstName = '%s' AND LastName = '%s' AND isDeleted = 0" % (ogfn,ogln))
    s = cursor.fetchall()
    id = s[0][0]
    print(id)

    cursor.execute("UPDATE Clients SET FirstName = '%s', LastName = '%s', dob = '%s',Email = '%s', Phone = '%s' WHERE ClientID = '%s'" % (fn,ln,dob,email,phone,id))
    db.commit()

    print("Update complete")

def performOAupdate(attyid,fn,ln):
    cursor.execute("SELECT ClientID FROM Clients WHERE FirstName = '%s' AND LastName = '%s'" % (fn,ln))
    c = cursor.fetchall()
    clientid = c[0][0]

    cursor.execute("UPDATE Clients SET OpposingAttorneyID = '%s' WHERE ClientID = '%s'" % (attyid,clientid))

def performGCIupdate(info,description):
    cursor.execute("UPDATE GeneralCaseInfo SET CaseName = '%s', Description = '%s'" % (info,description))

def performCourthouseUpdate(id,fn,ln,option):
    cursor.execute("SELECT ClientID FROM Clients WHERE FirstName = '%s' AND LastName = '%s'" % (fn,ln))
    r = cursor.fetchall()
    clientid = r[0][0]
    cursor.execute("SELECT CourthouseID FROM Courthouse WHERE Courthouse = '%s'" % (option))
    i = cursor.fetchall()
    courtid=i[0][0]
    cursor.execute("UPDATE Clients SET CourthouseID = '%s' WHERE ClientID = '%s'"% (courtid,clientid))
######################################################################################################################################################################################################################

#Root frame
root = Tk()
root.geometry("1000x1000")
#canvas = Canvas(root)

helloScreen = Frame(root, highlightbackground="black", highlightthickness=1)
helloScreen.place(relwidth=.9, relheight=.9, relx=.05,rely=.03)
greetings = Label(helloScreen, text="Welcome to the database \nPlease select an option",)
greetings.place(rely=.1,relx=.45)

# Search button for client name
searchButton = Button(helloScreen, text="Search", fg="green", width=85,height=3, command=searchPage)
searchButton.place(relx=.15, rely=.5)

# Insert button to add something to the db
insertButton = Button(helloScreen, text="Add", fg="blue", width=85,height=3, command=insertScreen)
insertButton.place(relx=.15, rely=.6)

#Update button
updateButton = Button(helloScreen, text="Update", fg="purple",width=85,height=3,command=updateDecide)
updateButton.place(relx=.15, rely=.7)

# Delete button to soft delete a record from a table based off a name
deleteButton = Button(helloScreen, text="Delete", fg="red", width=85,height=3,command=deleteScreen)
deleteButton.place(relx=.15, rely=.8)

genReport = Button(helloScreen,text="Generate Report", command=generateReportScreen)
genReport.place(relx=.8,rely=.9)

root.mainloop()

