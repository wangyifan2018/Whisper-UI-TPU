# Whisper-WebUI For Sophgo Whisper
A Gradio-based browser interface for [Whisper](https://github.com/openai/whisper). You can use it as an Easy Subtitle Generator!

Powered by [Whisper-WebUI](https://github.com/jhj0517/Whisper-WebUI/tree/master)

![Whisper WebUI](./screenshot.jpg)

## Notebook

# Feature
- Generate subtitles from various sources, including :
  - Files
  - Youtube
  - Microphone
- Currently supported subtitle formats :
  - SRT
  - WebVTT
  - txt ( only text file without timeline )
- Speech to Text Translation
  - From other languages to English. ( This is Whisper's end-to-end speech-to-text translation feature )


# Installation and Running
## Prerequisite
To run this WebUI, you need to have `git`, `python` version 3.8 ~ 3.10, `Sophon driver`  and `FFmpeg`.

Please follow the links below to install the necessary software:
- Driver : [https://doc.sophgo.com/sdk-docs/v23.09.01-lts/docs_latest_release/docs/SophonSDK_doc/zh/html/sdk_intro/4_install.html#id8](https://doc.sophgo.com/sdk-docs/v23.09.01-lts/docs_latest_release/docs/SophonSDK_doc/zh/html/sdk_intro/4_install.html#id8)
- git : [https://git-scm.com/downloads](https://git-scm.com/downloads)
- python : [https://www.python.org/downloads/](https://www.python.org/downloads/) **( If your python version is too new, torch will not install properly.)**
- FFmpeg :  [https://doc.sophgo.com/sdk-docs/v23.09.01-lts/docs_latest_release/docs/SophonSDK_doc/zh/html/sdk_intro/4_install.html#id9](https://doc.sophgo.com/sdk-docs/v23.09.01-lts/docs_latest_release/docs/SophonSDK_doc/zh/html/sdk_intro/4_install.html#id9)
- Sail : [https://doc.sophgo.com/sdk-docs/v23.10.01/docs_latest_release/docs/sophon-sail/docs/zh/html/1_build.html#](https://doc.sophgo.com/sdk-docs/v23.10.01/docs_latest_release/docs/sophon-sail/docs/zh/html/1_build.html#)


### Sail PCIe Platform
If you have installed a PCIe accelerator card (such as the SC series accelerator cards) on an x86/arm platform and are using it to test this routine, you will need to install libsophon, sophon-opencv, and sophon-ffmpeg. For specific installation instructions, please refer to the development and runtime environment setup for the x86-pcie platform or the arm-pcie platform.

Additionally, you will need to install other third-party libraries:
```bash
pip3 install -r requirements.txt
```
You will also need to install sophon-sail. Since the version of sophon-sail required by this routine is quite new and its related features have not yet been released, we are temporarily providing a usable version of sophon-sail. The x86/arm PCIe environment can download it with the following commands:
```bash
pip3 install dfss --upgrade #安装dfss依赖

#x86 pcie, py38
python3 -m dfss --url=open@sophgo.com:sophon-demo/Whisper/sail/pcie/sophon-3.7.0-py3-none-any.whl
pip3 install sophon-3.7.0-py3-none-any.whl

#arm pcie, py38
python3 -m dfss --url=open@sophgo.com:sophon-demo/Whisper/sail/arm_pcie/sophon_arm_pcie-3.7.0-py3-none-any.whl
pip3 install sophon_arm_pcie-3.7.0-py3-none-any.whl
```

If you need other versions of sophon-sail, or if you encounter issues with the glibc version (which is common in pcie environments), you can download the source code with the following command and compile sophon-sail yourself by referring to the [sophon-sail compilation and installation guide](https://doc.sophgo.com/sdk-docs/v23.10.01/docs_latest_release/docs/sophon-sail/docs/zh/html/1_build.html#).
```bash
python3 -m dfss --url=open@sophgo.com:sophon-demo/Whisper/sail/sophon-sail_20240226.tar.gz
tar xvf sophon-sail_20240226.tar.gz
```

### Sail SoC Platform
If you are using an SoC platform (such as the SE, SM series edge devices) and are using it to test this routine, the corresponding libsophon, sophon-opencv, and sophon-ffmpeg runtime library packages are already pre-installed in /opt/sophon/ after flashing the device.

In addition, you will need to install other third-party libraries:
```bash
pip3 install -r requirements.txt
```
Since the version of sophon-sail required by this routine is quite new, we are providing a usable sophon-sail whl package. The SoC environment can download it with the following command:
```bash
pip3 install dfss --upgrade
python3 -m dfss --url=open@sophgo.com:sophon-demo/ChatGLM3/sail/soc/sophon_arm-3.7.0-py3-none-any.whl #arm soc, py38
```
If you need other versions of sophon-sail, you can refer to the previous section and compile it yourself after downloading the source code.

After installing FFmpeg, **make sure to add the `FFmpeg/bin` folder to your system PATH!**
```bash
export PATH=$PATH:/opt/sophon/sophon-ffmpeg-latest/bin
```

## Automatic Installation
If you have satisfied the prerequisites listed above, you are now ready to start Whisper-WebUI.

1. Run `install.sh`
2. Run `start-webui.sh`
3. Open your web browser and go to `http://localhost:7860`

( If you're running another Web-UI, it will be hosted on a different port , such as `localhost:7861`, `localhost:7862`, and so on )


