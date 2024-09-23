import pytest
from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient
from .conftest import test_client


route_list = [
    "/",
    "api/fn011",
    "api/fn012",
    "api/fn022",
    "api/fn026",
    "api/fn026_subspace",
    "api/fn028",
    "api/fn121",
    "api/fn121_electrofishing",
    "api/fn121_gps_tracks",
    "api/fn122",
    "api/fn123",
    "api/fn123_nonfish",
    "api/fn124",
    "api/fn125",
    "api/fn125_lamprey",
    "api/fn125_tag",
    "api/fn126",
    "api/fn127",
    "api/gear_effort_proctype",
    "api/stream_dimensions",
]


@pytest.mark.parametrize("url", route_list)
def test_health_check_with_fixture(test_client: TestClient, url: str) -> None:
    with test_client as client:
        response = client.get(url)
        assert response.status_code == HTTP_200_OK
