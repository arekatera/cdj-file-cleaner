import os
from pydub import AudioSegment

def read_config(config_file):
    config = {}
    with open(config_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def convert_to_16bit_1440kbps_wav(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".wav") or file.endswith(".flac"):
                # Create the corresponding output directory
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # Convert and save the file if it doesn't already exist
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".wav")
                
                if not os.path.exists(output_file_path):
                    audio = AudioSegment.from_file(input_file_path)
                    audio = audio.set_frame_rate(44100).set_sample_width(2)  # 16-bit depth
                    audio.export(output_file_path, format="wav", bitrate="1440k")
                    print(f"Converted {file} to 16-bit 1440kbps WAV and saved to {output_file_path}")
                else:
                    print(f"Skipped {file} as it already exists in the output folder")

# Read config file
config = read_config('config.txt')

input_folder = config['input_folder']
output_folder = config['output_folder']

convert_to_16bit_1440kbps_wav(input_folder, output_folder)