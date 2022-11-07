from PyPDF2 import PdfFileReader, PdfFileWriter
from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class params(BaseModel):
    pdf:str = None
    rotate:int = None
    page:int = None

@app.get("/")
def hello():
    return {"text":"Rotate pdf "}
        
@app.post("/")
def read_user(body: params):
    body=body.dict()
    return  rotatepdf(body["pdf"],body["rotate"],body["page"])


def rotatepdf(file_path:str,angle_of_rotation:int,page_number:int) :
    targetfile = file_path
    outfile = open("/tmp/result.pdf", "wb")
    pdf = PdfFileReader(targetfile)
    writer = PdfFileWriter()
    numPages = pdf.getNumPages()
    num = page_number -1
    angle = angle_of_rotation % 360
    for i in range(numPages):
        if i == num :
            page = pdf.getPage(i)
            page.rotateClockwise(angle)
            writer.addPage(page)
        else :
            page = pdf.getPage(i)
            page.rotateClockwise(0)
            writer.addPage(page)

    writer.write(outfile)
    outfile.close()
    return {"file_path" :"/tmp/result.pdf","angle_of_rotation":angle,"page_number":page_number}
    

    