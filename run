#!/bin/bash

install_python() {
  if pyenv versions | grep -q '3.10'; then
    echo "Python 3.10 is already installed."
  else
    curl https://pyenv.run | bash

    {
      echo "export PYENV_ROOT=\"$HOME/.pyenv\""
      echo "command -v pyenv >/dev/null || export PATH=\"$PYENV_ROOT/bin:\$PATH\""
      echo "eval \"\$(pyenv init -)\""
    } >> ~/.bashrc

    {
      echo "export PYENV_ROOT=\"$HOME/.pyenv\""
      echo "command -v pyenv >/dev/null || export PATH=\"$PYENV_ROOT/bin:\$PATH\""
      echo "eval \"\$(pyenv init -)\""
    } >> ~/.profile

    sudo apt update
    sudo apt install -y build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

    pyenv install 3.10
    pyenv global 3.10
  fi

  pip install -r requirements.txt
}

run_program() {
  python start.py
}

while true; do
  echo "Select an option:"
  echo "1) Install"
  echo "2) Run"
  echo "3) Exit"
  read -rp "Enter your choice: " choice

  case $choice in
    1)
      install_python
      ;;
    2)
      run_program
      ;;
    3)
      exit 0
      ;;
    *)
      echo "Invalid option. Please try again."
      ;;
  esac
done
