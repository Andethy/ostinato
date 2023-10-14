TONICS_STR = {b: a for a, b in enumerate(('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'))}
TONICS_INT = {a: b for a, b in enumerate(('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'))}
print(TONICS_STR)
SCALES = {
    "ionian": (0, 2, 4, 5, 7, 9, 11),
    "aeolian": (0, 2, 3, 5, 7, 8, 10),
    "dorian": (0, 2, 3, 5, 7, 9, 10),
    "phrygian": (0, 1, 3, 5, 7, 8, 10),
    "harmonic": (0, 2, 3, 5, 7, 8, 11),
    "dominant-phrygian": (0, 1, 4, 5, 7, 8, 10),
    "jazz-minor": (0, 2, 3, 5, 7, 9, 11)}

HARMONIES = {
    "major-triad": (0, 4, 7),
    "minor-triad": (0, 3, 7),
    "dim-triad": (0, 3, 6),
    "aug-triad": (0, 4, 8),
    "sus2-triad": (0, 2, 7),
    "sus4-triad": (0, 5, 7),
    "major-7th": (0, 4, 7, 11),
    "minor-7th": (0, 3, 7, 10),
    "major-9th": (0, 4, 7, 11, 14),
    "minor-9th": (0, 3, 7, 10, 14)}

HARMONY_KEYS = HARMONIES.keys()

UNUSED = {
    "perfect-5th": (0, 7),
}

MID_OFFSET = 48
BASS_OFFSET = MID_OFFSET - 24
SUB_OFFSET = MID_OFFSET - 36
MELODY_OFFSET = MID_OFFSET + 12
