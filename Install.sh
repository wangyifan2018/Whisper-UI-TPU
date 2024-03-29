#!/bin/bash
pip install -r requirements.txt

echo ""
echo "Requirements installed successfully."

python3 -m dfss --url=open@sophgo.com:sophon-demo/Whisper/model_240327/models.zip
unzip models.zip
rm models.zip
echo "Models download successfully."