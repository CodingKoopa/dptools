
## Main Loop
- ABXY: Soft reset.

## Memory Allocation
Generally, DS games have the ARM9 binary loaded into RAM, then the overlays, and then the rest of the RAM is dedicated to the arena, used for dynamic memory allocation. Pokémon Diamond has a system for managing overlays, but the way it uses the arena is a little different.

## Message Data
The source message data for this game is found in `pm_dp_ose/convert/message/src`, in XML files with the extension `gmm`.

### GMM File Format
These files are generated and edited with the MessageEditor program, which we don't have (to my knowledge). The existence of this program is indicated by the attribute of the `generator` tag, and the contents of `pm_dp_ose/convert/message/src/me.bat`.

#### Header
GMM files start with:
- The usual XML header (`xml`, `xml-sytlesheet`)
- A `gmml` tag (GM Markup Language, perhaps?), with a `version` attribute.
  - There are no references to anything like this online that make sense in the context of a message editor. This is likely terminology internal to GameFreak.

#### Body

##### Boilerplate
Every GMM file seems to have the same boilerplate:
- A `color` element with `list` tags.
- A `tag-table` element with groups and tags inside.
- A `columns` element with information about the text inside, including font.
- A `dialog` element with information that looks to have to do with MessageEditor functionality.
- An `output` element. Not sure what this does.
- A `lock` element. Not sure what this does.

I'm not sure what purpose a lot of this boilerplate serves.

##### Rows
In each GMM file, for each message, there is a `row` element with an `id` attribute, the element containing:
- A `comment` element specifying the context for the message.
  - This often uses `♂` and `♀` to specify the gender of the speaker.
  - If a parameter is used in the `language`, it will be specified here.
- An `attribute` element for message metadata.
  - This has a `name` attribute for specifying what the `attribute` is. So far, I have only seen this be used to specify what character is saying the message.
- A `language` element specifying the message.
  - This has a `name` attribute for specifying the language.
  - This can use parameters like `[1:03:トレーナー名:0]` to insert things like the player's name into the text.