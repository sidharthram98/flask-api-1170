from ubuntu
copy . .
run apt-get update -y && apt install git python3-pip curl wget -y
run pip3 install -r requirements.txt
entrypoint ["python3"]
cmd ["run.py"]
