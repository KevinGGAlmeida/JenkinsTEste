FROM  python

WORKDIR /app

RUN python -m pip install selenium pyscreenshot pandas pillow openpyxl flask

COPY . .

CMD ["python","app.py"]
