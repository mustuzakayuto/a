import io
import os

import modal

stub = modal.Stub()


@stub.function(
    image=modal.Image.debian_slim().pip_install("torch", "diffusers[torch]", "transformers", "ftfy",'uvicorn==0.21.1','pyOpenSSL==23.1.1','numpy==1.23.5','torch==2.0.1','torchaudio==2.0.2','resampy==0.4.2','python-socketio==5.8.0','fastapi==0.95.1','python-multipart==0.0.6','onnxruntime-gpu==1.13.1','scipy==1.10.1','matplotlib==3.7.1','websockets==11.0.2','faiss-cpu==1.7.3','torchcrepe==0.0.18','librosa==0.9.1','gin==0.1.6','gin_config==0.5.0','einops==0.6.0','local_attention==1.8.5','websockets==11.0.2','sounddevice==0.4.6','dataclasses_json==0.5.7','onnxsim==0.4.28',"GitPython","pyngrok","fairseq","pyworld")
    .apt_install(
        "git",
        "python3-pyaudio"
    )
    .run_commands(
        "git clone https://github.com/w-okada/voice-changer.git",
        
        
    ),
    secret=modal.Secret.from_name("vcclient"),
    
    
    gpu="any",
    # 3時間でタイムアウト
    timeout=60*60*3,
)
async def run_stable_diffusion():
    
    
    
    
    os.chdir("/voice-changer/server")
    port = 18888
    from pyngrok import ngrok, conf
    # accesstoken
    conf.get_default().auth_token = ""
    # domain
    public_url = ngrok.connect(port,hostname="")
    print(f"ngrok URL: {public_url}")
    
    import subprocess
    subprocess.run(["python", "MMVCServerSIO.py"])
   

@stub.local_entrypoint()
def main():
    img_bytes = run_stable_diffusion.remote()
