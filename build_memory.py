from memvid import MemvidEncoder

chunks = [
    "Jean-Luc Picard is captain of the enterprise",
    "William Riker is first officer",
    "Data is an android",
    "Data is the second in command",
    "Picard's rank is Captain",
    "Riker's rank is Commander",
    "Data's rank is Lieutenant Commander",
    "The Enterprise runs on impulse and warp drives",
    "Impulse drive ejects low energy plasma to generate thrust at lower than light speeds",
    "Warp drive uses matter-antimatter reactions to generate a warp field through which the ship can move at locally slow speeds, but globally faster-than-light speeds",
    "The enterprise is armed with phasers, photon torpedoes, and a rock launcher"
]

encoder = MemvidEncoder()
encoder.add_chunks(chunks)
encoder.build_video("memory.mp4", "memory_index.json")
