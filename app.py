import gradio as gr
import os
import argparse

from modules.whisper_Inference import WhisperInference
from ui.htmls import *
from modules.youtube_manager import get_ytmetas

class App:
    def __init__(self, args):
        self.args = args
        self.app = gr.Blocks(css=CSS, theme=self.args.theme)
        self.whisper_inf = WhisperInference()

        print("Use Sophgo Whisper implementation")

    @staticmethod
    def open_folder(folder_path: str):
        if os.path.exists(folder_path):
            os.system(f"start {folder_path}")
        else:
            print(f"The folder {folder_path} does not exist.")

    @staticmethod
    def on_change_models(model_size: str):
        translatable_model = ["large", "large-v1", "large-v2", "large-v3"]
        if model_size not in translatable_model:
            return gr.Checkbox(visible=False, value=False, interactive=False)
        else:
            return gr.Checkbox(visible=True, value=False, label="Translate to English?", interactive=True)

    def launch(self):
        with self.app:
            with gr.Row():
                with gr.Column():
                    gr.Markdown(MARKDOWN, elem_id="md_project")
            with gr.Tabs():
                with gr.TabItem("File"):  # tab1
                    with gr.Row():
                        input_file = gr.Files(type="filepath", label="Upload File here")
                    with gr.Row():
                        dd_model = gr.Dropdown(choices=self.whisper_inf.available_models, value="base",
                                               label="Model")
                        dd_lang = gr.Dropdown(choices=["Automatic Detection"] + self.whisper_inf.available_langs,
                                              value="Automatic Detection", label="Language")
                        dd_file_format = gr.Dropdown(["SRT", "WebVTT", "txt"], value="SRT", label="File Format")
                    with gr.Row():
                        cb_translate = gr.Checkbox(value=False, label="Translate to English?", interactive=True)
                    with gr.Row():
                        cb_timestamp = gr.Checkbox(value=True, label="Add a timestamp to the end of the filename", interactive=True)
                    with gr.Accordion("Advanced_Parameters", open=False):
                        nb_beam_size = gr.Textbox(label="Initial Prompt", placeholder="Type something here...", lines=2)
                        nb_log_prob_threshold = gr.Number(label="Log Probability Threshold", value=-1.0, interactive=True)
                        nb_no_speech_threshold = gr.Number(label="No Speech Threshold", value=0.6, interactive=True)
                    with gr.Row():
                        btn_run = gr.Button("GENERATE SUBTITLE FILE", variant="primary")
                    with gr.Row():
                        tb_indicator = gr.Textbox(label="Output", scale=4)
                        files_subtitles = gr.Files(label="Downloadable output file", scale=4, interactive=False)
                        btn_openfolder = gr.Button('📂', scale=1)

                    params = [input_file, dd_model, dd_lang, dd_file_format, cb_translate, cb_timestamp]
                    advanced_params = [nb_beam_size, nb_log_prob_threshold, nb_no_speech_threshold]
                    btn_run.click(fn=self.whisper_inf.transcribe_file,
                                  inputs=params + advanced_params,
                                  outputs=[tb_indicator, files_subtitles])
                    btn_openfolder.click(fn=lambda: self.open_folder("outputs"), inputs=None, outputs=None)
                    dd_model.change(fn=self.on_change_models, inputs=[dd_model], outputs=[cb_translate])

                with gr.TabItem("Youtube"):  # tab2
                    with gr.Row():
                        tb_youtubelink = gr.Textbox(label="Youtube Link")
                    with gr.Row(equal_height=True):
                        with gr.Column():
                            img_thumbnail = gr.Image(label="Youtube Thumbnail")
                        with gr.Column():
                            tb_title = gr.Label(label="Youtube Title")
                            tb_description = gr.Textbox(label="Youtube Description", max_lines=15)
                    with gr.Row():
                        dd_model = gr.Dropdown(choices=self.whisper_inf.available_models, value="base",
                                               label="Model")
                        dd_lang = gr.Dropdown(choices=["Automatic Detection"] + self.whisper_inf.available_langs,
                                              value="Automatic Detection", label="Language")
                        dd_file_format = gr.Dropdown(choices=["SRT", "WebVTT", "txt"], value="SRT", label="File Format")
                    with gr.Row():
                        cb_translate = gr.Checkbox(value=False, label="Translate to English?", interactive=True)
                    with gr.Row():
                        cb_timestamp = gr.Checkbox(value=True, label="Add a timestamp to the end of the filename",
                                                   interactive=True)
                    with gr.Accordion("Advanced_Parameters", open=False):
                        nb_beam_size = gr.Textbox(label="Initial Prompt", placeholder="Type something here...", lines=2)
                        nb_log_prob_threshold = gr.Number(label="Log Probability Threshold", value=-1.0, interactive=True)
                        nb_no_speech_threshold = gr.Number(label="No Speech Threshold", value=0.6, interactive=True)
                    with gr.Row():
                        btn_run = gr.Button("GENERATE SUBTITLE FILE", variant="primary")
                    with gr.Row():
                        tb_indicator = gr.Textbox(label="Output", scale=4)
                        files_subtitles = gr.Files(label="Downloadable output file", scale=4)
                        btn_openfolder = gr.Button('📂', scale=1)

                    params = [tb_youtubelink, dd_model, dd_lang, dd_file_format, cb_translate, cb_timestamp]
                    advanced_params = [nb_beam_size, nb_log_prob_threshold, nb_no_speech_threshold]
                    btn_run.click(fn=self.whisper_inf.transcribe_youtube,
                                  inputs=params + advanced_params,
                                  outputs=[tb_indicator, files_subtitles])
                    tb_youtubelink.change(get_ytmetas, inputs=[tb_youtubelink],
                                          outputs=[img_thumbnail, tb_title, tb_description])
                    btn_openfolder.click(fn=lambda: self.open_folder("outputs"), inputs=None, outputs=None)
                    dd_model.change(fn=self.on_change_models, inputs=[dd_model], outputs=[cb_translate])

                with gr.TabItem("Mic"):  # tab3
                    with gr.Row():
                        mic_input = gr.Microphone(label="Record with Mic", type="filepath", interactive=True)
                    with gr.Row():
                        dd_model = gr.Dropdown(choices=self.whisper_inf.available_models, value="base",
                                               label="Model")
                        dd_lang = gr.Dropdown(choices=["Automatic Detection"] + self.whisper_inf.available_langs,
                                              value="Automatic Detection", label="Language")
                        dd_file_format = gr.Dropdown(["SRT", "WebVTT", "txt"], value="SRT", label="File Format")
                    with gr.Row():
                        cb_translate = gr.Checkbox(value=False, label="Translate to English?", interactive=True)
                    with gr.Accordion("Advanced_Parameters", open=False):
                        nb_beam_size = gr.Textbox(label="Initial Prompt", placeholder="Type something here...", lines=2)
                        nb_log_prob_threshold = gr.Number(label="Log Probability Threshold", value=-1.0, interactive=True)
                        nb_no_speech_threshold = gr.Number(label="No Speech Threshold", value=0.6, interactive=True)
                    with gr.Row():
                        btn_run = gr.Button("GENERATE SUBTITLE FILE", variant="primary")
                    with gr.Row():
                        tb_indicator = gr.Textbox(label="Output", scale=4)
                        files_subtitles = gr.Files(label="Downloadable output file", scale=4)
                        btn_openfolder = gr.Button('📂', scale=1)

                    params = [mic_input, dd_model, dd_lang, dd_file_format, cb_translate]
                    advanced_params = [nb_beam_size, nb_log_prob_threshold, nb_no_speech_threshold]
                    btn_run.click(fn=self.whisper_inf.transcribe_mic,
                                  inputs=params + advanced_params,
                                  outputs=[tb_indicator, files_subtitles])
                    btn_openfolder.click(fn=lambda: self.open_folder("outputs"), inputs=None, outputs=None)
                    dd_model.change(fn=self.on_change_models, inputs=[dd_model], outputs=[cb_translate])


        # Launch the app with optional gradio settings
        launch_args = {}
        if self.args.share:
            launch_args['share'] = self.args.share
        if self.args.server_name:
            launch_args['server_name'] = self.args.server_name
        if self.args.server_port:
            launch_args['server_port'] = self.args.server_port
        if self.args.username and self.args.password:
            launch_args['auth'] = (self.args.username, self.args.password)
        self.app.queue(api_open=False).launch(**launch_args)


# Create the parser for command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--share', type=bool, default=False, nargs='?', const=True, help='Gradio share value')
parser.add_argument('--server_name', type=str, default=None, help='Gradio server host')
parser.add_argument('--server_port', type=int, default=None, help='Gradio server port')
parser.add_argument('--username', type=str, default=None, help='Gradio authentication username')
parser.add_argument('--password', type=str, default=None, help='Gradio authentication password')
parser.add_argument('--theme', type=str, default=None, help='Gradio Blocks theme')
_args = parser.parse_args()

if __name__ == "__main__":
    app = App(args=_args)
    app.launch()
