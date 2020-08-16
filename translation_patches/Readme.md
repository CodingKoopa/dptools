# Translation Patches
This directory contains patches for translating the prototype. These are *very* rough translations, as they were done entirely with machine translation - particularly [DeepL Translate](https://www.deepl.com/translator) and [Google Translate](https://translate.google.com/) (but mostly the former, as Google Translate tends to do a poorer job).

## Translation Notes

### General
- Messages shown when playing as the male protagonist are prioritized.
- "Mandatory" messages are prioritized, although some optional NPC text is translated.
  - Text for objects (e.g. bookshelves) are very low priority.
- In any cases where there were substitutions for the player's name, they were harcoded to "Lucas", to make things easier.
- The ingame text sometimes indicates who is speaking, e.g. `ママ『おはよう！` to indicate that mom (ママ) is saying "おはよう！" I didn't think this was in the final game, but it actually is, so whoops. This translation doesn't have this, at least not right now.
- I have to do the linewrapping myself, so that may be off at times (e.g. text doesn't take up as much of the box as it could).
- There are two types of arrows that can be used to advance the text. I haven't really looked into how this mechanic works, and have just used the `▼` arrow, rather than `▽`.

### Player Home (Twinleaf Town)
The tricky part about translating this scene was the part about visiting the player's father. The mother talks about the player meeting their father by some body of water. I have interpreted this as going to Lake Verity, as there is an encounter with the father there.

### Twinleaf Town
It's unclear to me what it is that Rowan drops here, when bumping into the player. I have made my best guess in assuming that he dropped the Pokémon case. The only issue with this is that the Lake Verity dialog seems to hint at Rowan giving the player *back* the Pokédex, as if the Pokédex is what Rowan had dropped.

### Route 201
These messages were pretty straightforward. The only "issue" is that it was a little awkward translating Barry's text with every sentence having an exclamation mark. Oh well, guess that's Barry for you.

### Lake Verity
This was definitely the hardest set of messages to translate. Some of the issues:
- There are remenants of an older version of this sequence here. In a past version (specifically, a "2/17" version) of this sequence, it seems that a wild Pokémon jumped out and stole his Pokédex. I have done my best to stub out this past version for some kind of consistency.
  - In order to achieve this, the usage of the "dummy" message in the script was removed.
- It's unclear to me how exactly Rowan addresses Lucas in giving him the Pokédex and Pokémon in the original text. This I mostly had to make up.
- In some cases, the received Pokémon will be referred to with it's Japanese. I have already translated some of the Pokémon names in once place, so I'm not sure where else to patch it.
- I don't understand why the player originally had to meet his dad here. His mom had told him to meet him, as if there was some sort of business that had to be discussed, yet his dad only talks about the business with Rowan that had only happened to come up *after* the mom had sent the player to Lake Verity.

### Sandgem Town
Dawn's text was a little tricky, but nothing too bad.

### Rowan's Lab (Sandgem Town)
This was okay.
- Rowan never seems to address the Pokémon case that he had forgotten (and the automatic translation of the father's text really does seem to indicate that that had been the case).
- The text `msg_t02r0101_oldwoman1a_01` is interesting, as it is for an old woman who is not in the final game. However, her text does not automatically translate well at all, and I don't have anything in the final game to work off of, so I have neglected to translate this one in particular.

### Route 202
The catching tutorial is mentioened by the original text, even though it is not implemented ingame. I have kept this.