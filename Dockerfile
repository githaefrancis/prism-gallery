FROM python:3.8-alpine3.17

WORKDIR /usr/src/prism_gallery

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/ofasnplugs/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/prism_gallery/entrypoint.sh"]

COPY . .

ENTRYPOINT ["sh","/usr/src/prism_gallery/entrypoint.sh"]