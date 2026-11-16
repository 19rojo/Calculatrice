# run.py
import subprocess
import sys

def main():
    # Lancement de Tailwind en arrière-plan
    tailwind_process = subprocess.Popen([
        "npx.cmd", "@tailwindcss/cli", 
        "-i", "./static/css/input.css", 
        "-o", "./static/css/output.css", 
        "--watch"
    ])
    
    # Lancement de Flask
    flask_process = subprocess.Popen([
        sys.executable, "app.py"
    ])
    
    try:
        # Garde les processus actifs
        tailwind_process.wait()
        flask_process.wait()
    except KeyboardInterrupt:
        # Arrêt propre si tu fais Ctrl+C
        tailwind_process.terminate()
        flask_process.terminate()
        print("\nArrêt des services.")

if __name__ == "__main__":
    main()