from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao_fixture():
    director_dao = DirectorDAO(None)

    alex = Director(id=1, name="Alex")
    alina = Director(id=2, name="Alina")

    director_dao.get_one = MagicMock(return_value=alex)
    director_dao.get_all = MagicMock(return_value=[alex, alina])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert len(directors) == 2

    def test_create(self):
        director_data = {
            "name": "Rose"
        }

        director = self.director_service.create(director_data)
        assert director.id is not None

    def test_update(self):
        director_data = {
            "id": 1,
            "name": "Rose"
        }

        self.director_service.update(director_data)

    def test_delete(self):
        self.director_service.delete(1)