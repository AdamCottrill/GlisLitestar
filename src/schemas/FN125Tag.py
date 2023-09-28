from typing import Optional


from pydantic import constr, field_validator, PositiveInt, constr
from .FNBase import FNBase
from .utils import string_to_int, PRJ_CD_REGEX


tag_type_choices = {
    "0": "No tag  (Do Not Use. Historical data only.)",
    "1": "Streamer (Disc)",
    "2": "Tubular Vinyl (example-T Bar Anchor tag)",
    "3": "Circular Strap Jaw / Maxillary Tag",
    "4": "Butt End Jaw",
    "5": "Anchor",
    "6": "Coded Wire",
    "7": "Strip Vinyl",
    "8": "Secure Tie",
    "9": "Type Unknown or not applicable",
    "A": "Radio or Acoustic tag",
    "B": "Monel Metal Livestock",
    "C": "Cinch",
    "E": "Elastomer",
    "x": "Tag Scar/obvious loss",
    "P": "PIT tag",
}
tag_position_choices = {
    "1": "Anterior Dorsal",
    "2": "Between Dorsal",
    "3": "Posterior Dorsal",
    "4": "Abdominal Insertion",
    "5": "Flesh of Back* ",
    "6": "Jaw",
    "7": "Snout",
    "8": "Anal",
    "9": "Unknown",
}


tag_agency_choices = {
    "01": "Ontario Ministry of Natural Resources",
    "02": "New York State",
    "03": "State of Michigan",
    "04": "University of Guelph",
    "05": "University of Toronto",
    "06": "State of Ohio",
    "07": "State of Pennsylvania",
    "08": "Royal Ontario Museum",
    "09": "State of Minnesota",
    "10": "Lakehead University",
    "11": "Sir Sandford Fleming College",
    "12": "Private Club",
    "13": "Ontario Hydro",
    "19": "U.S.F.W.S.",
    "20": "U.S.G.S",
    "21": "State of Wisconsin (?)",
    "22": "State of Indiana (?)",
    "23": "State of Illinois (?)",
    "24": "CORA (?)  ",
    "25": "AOFRC = Anishinabek/Ontario Fisheries Resource Centre     ",
    "26": "GLLFAS =  Great Lakes Laboratory for Fisheries and Aquatic Sciences",
    "27": "Queen's University",
    "98": "Other",
    "99": "Unknown",
}
tag_colour_choices = {
    "1": "Colourless",
    "2": "Yellow",
    "3": "Red",
    "4": "Green",
    "5": "Orange",
    "6": "Silver (includes coded-wire tags)",
    "7": "White  ",
    "8": "Purple  ",
    "9": "Unknown",
    "A": "Gold",
    "B": "Black",
    "C": "Blue",
}


class FN125Tag(FNBase):
    """Pydantic model for fish tags.

    this model will be revisited after tag model is refactored -
    tagdoc needs to be split into distinct fields.  Similarly, attributes
    of tag on capture need to be split apart.

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")
    fish: int
    fish_tag_id: int
    tagid: Optional[str]
    tagdoc: constr(pattern="^([A-Z0-9]{5})$", to_upper=True, min_length=5, max_length=5)

    tagstat: constr(
        pattern="^(N|A2?|C([0134][1-49][1-49])?)$",
        to_upper=True,
        min_length=1,
        max_length=4,
    )

    cwtseq: Optional[PositiveInt] = None

    comment_tag: Optional[str]

    _string_to_int = field_validator("cwtseq", mode="before")(string_to_int)

    @field_validator("tagstat")
    @classmethod
    def check_tagstat_n(cls, value, values):
        """Tag stat N (checked and not found) is only appropriate for pit or cwts."""
        tagdoc = values.get("tagdoc")
        if tagdoc and value == "N":
            if tagdoc[0] not in ["P", "6"]:
                msg = "TAGSTAT='N' is only allowed if TAGTYPE is 6 (CWT) or P (PIT)."
                raise ValueError(msg)
        return value

    @field_validator("tagstat")
    @classmethod
    def check_null_tagid_if_tagstat_n(cls, value, values):
        """If tag stat is 'N' - tagid must be null. If you have a
        tagid, the tag was either applied or present on capture."""
        tagid = values["tagid"]
        if tagid and value == "N":
            msg = f"TAGSTAT cannot be 'N' if TAGID is populated (TAGID='{tagid}')."
            raise ValueError(msg)
        return value

    @field_validator("tagstat")
    @classmethod
    def check_null_tagid_if_tagstat_a(cls, value, values):
        """If tag stat is 'N' - tagid must be null. If you have a
        tagid, the tag was either applied or present on capture."""
        tagid = values["tagid"]
        if tagid is None and value == "A":
            msg = f"TAGID cannot be empty if TAGSTAT='A' (tag applied)."
            raise ValueError(msg)
        return value

    @field_validator("tagdoc")
    @classmethod
    def check_tag_type(cls, value, values):
        if value is not None:
            tag_type = value[0]
            if tag_type not in tag_type_choices:
                msg = f"Unknown tag_type code ({tag_type}) found in TAGDOC ({value})"
                raise ValueError(msg)
        return value

    @field_validator("tagdoc")
    @classmethod
    def check_tag_position(cls, value, values):
        if value is not None:
            tag_position = value[1]
            if tag_position not in tag_position_choices:
                msg = f"Unknown tag_position code ({tag_position}) found in TAGDOC ({value})"
                raise ValueError(msg)
        return value

    @field_validator("tagdoc")
    @classmethod
    def check_tag_agency(cls, value, values):
        if value is not None:
            agency = value[2:4]
            if agency not in tag_agency_choices:
                msg = f"Unknown tag_agency code ({agency}) found in TAGDOC ({value})"
                raise ValueError(msg)
        return value

    @field_validator("tagdoc")
    @classmethod
    def check_tag_colour(cls, value, values):
        if value is not None:
            tag_colour = value[4]
            if tag_colour not in tag_colour_choices:
                msg = (
                    f"Unknown tag_colour code ({tag_colour}) found in TAGDOC ({value})"
                )
                raise ValueError(msg)
        return value
