import docx
import argparse

#Initialize global variables to store the final output
data = {}
docrefno = set(data)

#Get the CLI from user with proper values and search operands.
parser = argparse.ArgumentParser(description="**** Python program to retrieve reference number of"
                                                     " pattern matched article*****",
                                             usage="doc_python AND care quality commission")
parser.add_argument('searchtype', type=str,choices=['And','Or','AND','OR','and','or'], help='Provide search type - either OR or AND')
parser.add_argument('stringtosearch', nargs='+', type=str, help='Provide string(s) to search')


args = parser.parse_args() #Parse the retrieved arguments
#Store them in seperate variables.


#To make the search operation simple, convert it to lowercase
searchtype = args.searchtype.lower() #searchtype holds the operations to perform.

searchstrings = args.stringtosearch  #Pattern to search  

document = docx.Document('hscic-news.docx')  #Get the input file document
table = document.tables[0]  #Get the tables from the document
              
for i, row in enumerate(table.rows):
    text = (cell.text for cell in row.cells)  #Get the content of each cell

    '''Pass the row and column headers silently '''
    if i == 0:
        continue
    
    stringPattern = ','.join(list(text)) #Get the string pattern as string from list
    
    #Search operations - Or    
    if searchtype=='or' :
        for searchstr in searchstrings:
            if searchstr in stringPattern:
                      docrefno.add(int(stringPattern[-1]))

        
    #Search operation - And
    if searchtype=='and':
        matchcnt=0
        for searchstr in searchstrings:                
            if searchstr in stringPattern:                                     
                  matchcnt+=1
                  if matchcnt == len(searchstrings):                    
                      docrefno.add(int(stringPattern[-1]))
                  continue
                    
print("The pattern to search :",searchstrings)
print("The type of search:",searchtype)
print("The document reference number is:", docrefno)



