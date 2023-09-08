from litestar import Litestar, get, MediaType


from utils import get_rows
from controllers import (
    FN011,
    FN012,
    FN022,
    FN026,
    FN026Subspace,
    FN028,
    FN121,
    FN122,
    FN123,
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
    [index, FN011, FN012, FN022, FN026, FN026Subspace, FN028, FN121, FN122, FN123]
)
