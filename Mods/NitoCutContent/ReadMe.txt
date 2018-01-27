This is a small mod that re-activates Gravelord Nito's cut content, with a few minor changes.

The way this was intended to work is that Nito would have a few areas on his body that would
act similar to a tail-cut, except when they were cut off, they would make the fight harder by
spawning additional skeletons. However, I can't get that part of it working because it seems
like the subpart of Nito was either removed or never created in the first place, or I'm just
doing it wrong. Instead, I've edited the event script file to make the events occur when Nito
reaches 75%, 50% and 25% of his health.

I've also edited Nito's team type so that he no longer obliterates his own skeletons with 
every attack. This was probably *not* part of the cut content, but the extra skeletons 
aren't particularly threatening otherwise.

I can't guarantee that the event will work perfectly, since I'm mostly just restoring cut 
content. It might be possible to break the event (and perhaps the whole boss fight) by quitting
at the wrong time, or taking some other action that this event was never tested against.

(If you're trying this out to see the event, it's probably better to not one- or two-shot 
Nito with Dark Bead, for instance, since the extra skeletons do not spawn once Nito dies.)

To install:

- Using UnpackDarkSoulsForModding (or if your game files are already unpacked).
 Use UDSFM to unpack your game files if they are not already.
 You can find UDSFM at https://www.nexusmods.com/darksouls/mods/1304/
 Make backups of \map\MapStudio\m13_01_00_00.msb and \event\m13_01_00_00.emevd
 Replace these files with the ones given.
- Using DS Drag & Drop Mod Manager
 No unpacking should be needed, just drag and drop the two files into the
 mod manager and use it to launch DS1.

This mod is not compatible with anything that modifies the two files.
In particular, anything that changes the placement of enemies or scripts in 
Tomb of the Giants will generally not be compatible.

To uninstall:

- Using UDSFM
 Restore the two files from the backup copies you made before installation
- Using DS Drag & Drop Mod Manager
 The modifications should be automatically reversed when you exit DS1.

== The details (skip if you don't want to know exactly what happens) == 

When Nito reaches each health threshold, he staggers backward
as a piece of the dangling skeletons on his front break off and shatter 
on the floor. These pieces then reform into two skeletons.

At the first threshold, two sword-wielding skeletons spawn.
At the second threshold, a sword-wielding skeleton and a bow-wielding skeleton spawn.
At the third threshold, a bow-wielding skeleton and a scimitar-wielding skeleton spawn.

Unfortunately, the original 6 skeletons were disabled in the map file, hence the new
.msb is needed to re-activate them. Additionally, they had cut NPC types. I've changed their
types to the ones mentioned above, but there no reason to expect this was originally the case.
However, the balance probably would have been similar, but perhaps these skeletons would have been
weaker or stronger, or entirely new. It's not really possible to tell.

==
