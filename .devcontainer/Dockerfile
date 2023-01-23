ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

RUN apt update && apt install zsh -y
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

ENV SHELL /bin/zsh

COPY .devcontainer/.zshrc $HOME

RUN pip install poetry
