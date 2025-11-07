from ollama_agent import ask_ollama


def main():
    print("Welcome to PokeChamp! Your Pokémon mentor is ready.")

    while True:
        question = input("\nAsk me something about Pokémon (or 'exit' to quit): ")
        if question.lower() == "exit":
            break

        answer = ask_ollama(question)
        print("\nPokeChamp says:", answer)


if __name__ == "__main__":
    main()
