from typing import Dict, List

DATA_TRANSFORMATION_CONFIG_BUCKET_NAME: str = "41644ecom-config"

DATA_TRANSFORMATION_ACRONYMS_CONFIG_FILE: str = "english_acronyms.json"

DATA_TRANSFORMATION_CONTRACTIONS_CONFIG_FILE: str = "english_contractions.json"

DATA_TRANSFORMATION_CONFIG_FOLDER: str = "config"

BEST_MODEL_FOLDER: str = "best_model"

BEST_MODEL_FILE_NAME: str = "model.pkl"

APP_HOST: str = "0.0.0.0"

APP_PORT: int = 8080

LABEL_DICT: Dict = {
    "Electronics": 0,
    "Household": 1,
    "Books": 2,
    "Clothing & Accessories": 3,
}

DATA_TRANSFORMATION_STOP_WORDS: List = [
    "among",
    "onto",
    "shall",
    "thrice",
    "thus",
    "twice",
    "unto",
    "us",
    "would",
]

DATA_TRANSFORMATION_KEEP_TAGS: List = [
    "NN",
    "NNS",
    "NNP",
    "NNPS",
    "FW",
    "PRP",
    "PRPS",
    "RB",
    "RBR",
    "RBS",
    "VB",
    "VBD",
    "VBG",
    "VBN",
    "VBP",
    "VBZ",
    "WDT",
    "WP",
    "WPS",
    "WRB",
]

ALPHABETS: List = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


PREPOSITIONS: List = [
    "about",
    "above",
    "across",
    "after",
    "against",
    "among",
    "around",
    "at",
    "before",
    "behind",
    "below",
    "beside",
    "between",
    "by",
    "down",
    "during",
    "for",
    "from",
    "in",
    "inside",
    "into",
    "near",
    "of",
    "off",
    "on",
    "out",
    "over",
    "through",
    "to",
    "toward",
    "under",
    "up",
    "with",
]

PREPOSITIONS_LESS_COMMON: List = [
    "aboard",
    "along",
    "amid",
    "as",
    "beneath",
    "beyond",
    "but",
    "concerning",
    "considering",
    "despite",
    "except",
    "following",
    "like",
    "minus",
    "onto",
    "outside",
    "per",
    "plus",
    "regarding",
    "round",
    "since",
    "than",
    "till",
    "underneath",
    "unlike",
    "until",
    "upon",
    "versus",
    "via",
    "within",
    "without",
]

COORDINATING_CONJUNCTIONS: List = ["and", "but", "for", "nor", "or", "so", "and", "yet"]

CORRELATIVE_CONJUNCTIONS = [
    "both",
    "and",
    "either",
    "or",
    "neither",
    "nor",
    "not",
    "only",
    "but",
    "whether",
    "or",
]

SUBORDINATING_CONJUNCTIONS: List = [
    "after",
    "although",
    "as",
    "as if",
    "as long as",
    "as much as",
    "as soon as",
    "as though",
    "because",
    "before",
    "by the time",
    "even if",
    "even though",
    "if",
    "in order that",
    "in case",
    "in the event that",
    "lest",
    "now that",
    "once",
    "only",
    "only if",
    "provided that",
    "since",
    "so",
    "supposing",
    "that",
    "than",
    "though",
    "till",
    "unless",
    "until",
    "when",
    "whenever",
    "where",
    "whereas",
    "wherever",
    "whether or not",
    "while",
]

OTHERS: List = [
    "ã",
    "å",
    "ì",
    "û",
    "ûªm",
    "ûó",
    "ûò",
    "ìñ",
    "ûªre",
    "ûªve",
    "ûª",
    "ûªs",
    "ûówe",
]
