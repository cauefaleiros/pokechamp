import subprocess


def ask_ollama(question, model="minimax-m2"):
    try:
        result = subprocess.run(
            ["ollama", "chat", model, "--prompt", question, "--cli"],
            capture_output=True,
            text=True,
        )
        if result.stdout.strip():
            return result.stdout.strip()
        else:
            return "Ollama não retornou nada. Tente outra pergunta."
    except FileNotFoundError:
        return "Ollama não encontrado. Verifique se está instalado e no PATH."
