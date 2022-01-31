FROM python:3.8-alpine as builder

# Set work directory.
WORKDIR /usr/src/app

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN set -ex && apk --no-cache add sudo

RUN pip install --upgrade pip
RUN pip install flake8==3.9.2
COPY . .
RUN flake8 --ignore=E501,F401 ./immo

#RUN apk --no-cache --update add libffi libressl postgresql-libs gcc libc-dev




#RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
#WORKDIR /django

#RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
# RUN apk add --no-cache gcc musl-dev linux-headers
# RUN apk update && apk add postgresql-dev gcc python-dev musl-dev

#RUN pip install -r requirements.txt
#RUN pip install versiontools
# RUN apk  add del .tmp
# RUN pip install -r /requirements.txt
RUN apk del .tmp
RUN apk add --no-cache tzdata
RUN pip install psycopg2-binary
ENV TZ America/Los_Angeles
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV TZ="America/New_York"
# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
#copy project

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Copy project code.

#########
# FINAL #
#########

# pull official base image
FROM python:3.8-alpine


# installing netcat (nc) since we are using that to listen to postgres server in entrypoint.sh
RUN apk update update && apk add install -y --no-install-recommends netcat && \
    apk add autoremove -y && \
    apk add clean && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Set work directory.
WORKDIR /usr/src/app

# copy entrypoint.prod.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy our mainproject
COPY ./mainproj .

# run entrypoint.prod.sh
RUN chmod +x  /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]