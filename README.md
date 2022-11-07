# REST_API_PDF_ROTATE

##How to run
1. git clone 
...bash
    git clone https://github.com/hemantp88/Rest_pdf_rotate.git
...

2. Have dependencies in requirements.txt (`pip install -r requirments.txt`)
3. run uvicorn using command uvicorn main:app 
4. Go to : http://localhost:8000/docs
    then select post /rotate

5. Try and execute 
        by clicking try it out and changes in schemna
        "pdf":"adreess of pdf file"
        "rotate": input angle of rotation
        "page": input the page t be rotated 

6. Rxecute
8. output will be generated in (/tmp/result.pdf)
