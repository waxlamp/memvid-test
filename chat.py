from memvid import MemvidChat


chat = MemvidChat("memory.mp4", "memory_index.json", llm_provider="openai")
chat.start_session()

while True:
    query = input("?>> ")
    if query == "quit":
        break
    print(chat.chat(query))
    print()
