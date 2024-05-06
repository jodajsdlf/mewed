import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# static(정적): file 내에서만 동작  = 움직일 일이 없다
# dynamic(동적): DB 또는 서버와 주고 받기

app = FastAPI()
# Jinja2 템플릿 엔진(HTML, CSS, JS)
templates = Jinja2Templates(directory="templates/")  # html 경로 지정하는 부분
app.mount("/assets", StaticFiles(directory="assets"), name="assets")  # css, img 파일들 경로 지정

#127.0.0.1:8000/ -> 실행
#127.0.0.1:8000/kakao
#127.0.0.1:8000/ -> 실행

@app.get("/")  # 매핑한 사이트
async def welcome(request: Request) :
    return templates.TemplateResponse("test.html",
                                      {"request": request})

# UVICORN WAS 주소 : 127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)