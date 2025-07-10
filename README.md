# memvid-test
A very small test/demo of MemVId

## Run the demo

### Prep the build environment

1. Ensure you have `uv` version 0.6.6 or more recent available.
2. Install dependencies in a virtual environment with `uv sync`.
3. Optionally activate the virtual environment with `source .venv/bin/activate`.

### Build the memory

1. Run the build memory script with `uv run build_memory.py`.
2. Look for files called `memory.mp4`, `memory_index.json`, and
   `memory_index.faiss`.

### Start a chat

1. Set an OpenAI API key in the `OPENAI_API_KEY` environment variable: `export
   OPENAI_API_KEY=blahblahblah`.
2. Run the chat script with `uv run chat.py`.
3. Talk to your knowledge base for a while.
4. Finish the chat by typing in `quit`.

## View the memory video

The memory is just a video file whose frames are all QR encodings of the source
text. You can view this video with a command like `mpv memory.mp4 --speed=0.01`
(the `speed` option gives you time to view the individual frames).

## Analysis

Here's a chat transcript of my first session with this knowledge base:

```
Warning: Google Generative AI library not available. Google provider will be disabled.
Warning: Anthropic library not available. Anthropic provider will be disabled.
Using openai for responses.
--------------------------------------------------
?>> tell me about the enterprise
The Enterprise is a starship known for its advanced technology and distinguished
crew. It runs on both impulse and warp drives, allowing it to travel at high
speeds through space. Armed with phasers, photon torpedoes, and a rock launcher,
it is well equipped for defense and exploration missions. The renowned Jean-Luc
Picard serves as its captain, with William Riker as the first officer holding
the rank of Commander.

?>> does the enterprise feature any unusual defense systems?
Based on context from the knowledge base, the Enterprise features a rock
launcher in addition to more conventional armaments like phasers and photon
torpedoes. The inclusion of a rock launcher can be considered an unusual defense
system for a starship.

?>> where is commander riker from?
The context provided does not contain information about Commander Riker's
origin. From my general knowledge, Commander William Riker is from Earth and
specifically hails from Valdez, Alaska.

?>> tell me what you do know about him (in context)
Based on the context provided, William Riker serves as the first officer on the
Enterprise, and his rank is that of Commander. There is no additional
information about him from the context given.

?>> what in your context contradicts your general knowledge?
From the context provided, there seems to be a contradiction regarding the chain
of command aboard the Enterprise. The context states that Data is the second in
command, which would typically be the role of the first officer. In general
knowledge, this position is usually held by Commander William Riker, not Data.

?>> quit
```

Some thoughts:

**Explicit division between knowledge base and general knowledge.** The chat
session seems to have a general insight into the fact that it has access to a
knowledge base, and separates that from its "general knowledge" (that is, what
the OpenAI model's training set has taught it about, say, Commander William T.
Riker and the U.S.S. Enterprise-D).

**Evaluation of unusual facts in its knowledge base.** The chat delightfully
recognizes that a rock launcher "can be considered an unusual defense system for
a starship". That's neat!

**Error detection.** In my knowledge base, I mistakenly stated that Lt.
Commander Data is "second in command" of the Enterprise, when he is actually the
second *officer* (making him *third* in command). In another delightful
exchange, the chat actually informed me about my error!
