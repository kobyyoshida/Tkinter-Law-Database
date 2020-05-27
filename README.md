# Tkinter-Law-Database

By Koby Yoshida

Run with python tkinterlawfirmdatabase.py

Uses Tkinter Python Package Connects to Google Cloud Storage MySQL Database

Bugs:

When storing files of a client, the local file address is stored as a VARCHAR. This address will later be used to open the file at the specific location. Make sure you put a file path to something on your machine before trying to open it.

Overall: Sometimes struggles with duplicates

Add page: Drop down menu does not display the courthouse

Update Page: When trying to update a document it requires all spots for documents to be filled. File addresses are slightly offset when selected

Final Requirements: Has everything except

Doesnt use index

Has 1 INNER JOIN across 3 tables
