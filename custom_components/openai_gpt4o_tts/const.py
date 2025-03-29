"""Constants for OpenAI GPT-4o Mini TTS integration."""

DOMAIN = "openai_gpt4o_tts"
PLATFORMS = ["tts"]

# Configuration keys
CONF_API_KEY = "api_key"
CONF_VOICE = "voice"
CONF_INSTRUCTIONS = "instructions"

# Default voice setting
DEFAULT_VOICE = "sage"

# Default multi-field instruction settings
DEFAULT_AFFECT = (
    "Veselý sprievodca, ktorý prednáša reč ako stand-up komik na kofeínovej vlne, "
    "drží poslucháča v napätí a zároveň ho navigujem ako GPS s doktorátom z dramaturgie."
)
DEFAULT_TONE = (
    "Priateľský, jasný a tak zábavný, že by rozosmial aj dopravný kužeľ, "
    "vytvára atmosféru, kde sa poslucháč smeje a zároveň si hovorí: 'Toto fakt funguje!'"
)
DEFAULT_PRONUNCIATION = (
    "Jasné, výstižné a s istotou, ako keby som hlásil víťaza v súťaži o najlepší vtip, "
    "každá inštrukcia zrozumiteľná, no s nádychom: 'Počúvaj ma, toto ti nevyjde bez môjho šarmu!'"
)
DEFAULT_PAUSE = (
    "Krátke, účelné prestávky po kľúčových pokynoch (napr. 'prejdi cez ulicu, ak sa nebojíš holubov' a 'odboč doprava, lebo inak si včera'), "
    "dávam poslucháčovi čas na chichot a nasledovanie bez toho, aby zaspal od nudy."
)
DEFAULT_EMOTION = (
    "Vrúcne a podporujúco, ako kamarát, ktorý ti fandí na karaoke, aj keď si mimo tóniny, "
    "s vtipnými hláškami typu: 'Neboj, tá skratka cez park nie je horor, len dobrodružstvo!'"
)
# Official GPT-4o TTS voices
OPENAI_TTS_VOICES = [
    "alloy",
    "ash",
    "ballad",
    "coral",
    "echo",
    "fable",
    "onyx",
    "nova",
    "sage",
    "shimmer"
]
