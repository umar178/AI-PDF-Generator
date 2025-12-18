import time
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import generator

app = FastAPI()
templates = Jinja2Templates(directory="pages")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    generator.log("Dashboard accessed.")
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
async def handle_generation(
    content: str = Form(...),
    pdf_type: str = Form(...),
    model_version: str = Form(...),
    include_images: bool = Form(False)
):
    start_time = time.time()
    generator.log(f"New Request -> Type: {pdf_type}, Model: {model_version}, Images: {include_images}")

    try:
        # Pass the UI selections to the generator function
        pdf_file_path = await generator.generate_pdf(
            content,
            pdf_type,
            model_name=model_version,
            use_images=include_images
        )

        duration = round(time.time() - start_time, 2)
        generator.log(f"Request completed successfully in {duration}s")

        return FileResponse(
            path=pdf_file_path,
            filename=f"generated_{pdf_type.lower().replace(' ', '_')}.pdf",
            media_type='application/pdf'
        )

    except Exception as e:
        generator.log(f"Request failed: {str(e)}", "ERROR")
        raise HTTPException(status_code=500, detail="Failed to generate PDF. Check console logs.")


if __name__ == "__main__":
    import uvicorn
    generator.log("Starting server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)