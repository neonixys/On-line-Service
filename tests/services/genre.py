from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao_fixture():
    genre_dao = GenreDAO(None)

    horror = Genre(id=1, name="Horror")
    science = Genre(id=2, name="Science")

    genre_dao.get_one = MagicMock(return_value=horror)
    genre_dao.get_all = MagicMock(return_value=[horror, science])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao_fixture):
        self.genre_service = GenreService(dao=genre_dao_fixture)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id == 1

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert genres is not None
        assert len(genres) > 0

    def test_create(self):
        genre_data = {
            "name": "Comedy"
        }

        genre = self.genre_service.create(genre_data)
        assert genre.id is not None

    def test_update(self):
        genre_data = {
            "id": 1,
            "name": "Comedy"
        }

        self.genre_service.update(genre_data)

    def test_delete(self):
        self.genre_service.delete(1)
