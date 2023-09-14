from litestar import Litestar, get, MediaType

from controllers import (
    FN011,
    FN012,
    FN022,
    FN026,
    FN026Subspace,
    FN028,
    FN121,
    FN121Electrofishing,
    FN121GpsTrack,
    FN122,
    FN123,
    FN123NonFish,
    FN124,
    FN125,
    FN125Lamprey,
    FN125Tag,
    FN126,
    FN127,
    GrEffProcType,
    StreamDimension,
)


@get(path="/", media_type=MediaType.HTML)
def index() -> str:
    return """
    <html>
        <body>
            <div>
                <span>THis will be the react app.</span>
            </div>
        </body>
    </html>
    """


app = Litestar(
    [
        index,
        FN011,
        FN012,
        FN022,
        FN026,
        FN026Subspace,
        FN028,
        FN121,
        FN121Electrofishing,
        FN121GpsTrack,
        FN122,
        FN123,
        FN123NonFish,
        FN125,
        FN125Lamprey,
        FN125Tag,
        FN124,
        FN126,
        FN127,
        GrEffProcType,
        StreamDimension,
    ]
)
