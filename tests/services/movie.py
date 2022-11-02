from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao_fixture():
    movie_dao = MovieDAO(None)

    d1 = Director(id=1, name="Alex D. Gold")
    g1 = Genre(id=1, name="Comedy")

    d2 = Director(id=2, name="Gold")
    g2 = Genre(id=2, name="Horror")

    movie1 = Movie(
        id=1,
        title="Джанго освобожденный",
        description="Эксцентричный охотник за головами, также известный как Дантист, промышляет отстрелом самых опасных преступников. Работенка пыльная, и без надежного помощника ему не обойтись. Но как найти такого и желательно не очень дорогого? Освобождённый им раб по имени Джанго – прекрасная кандидатура. Правда, у нового помощника свои мотивы – кое с чем надо сперва разобраться.",
        trailer="https://www.youtube.com/watch?v=2Dty-zwcPv4",
        year=2012,
        rating=8.4,
        genre=g1,
        director=d1,
        genre_id=17,
        director_id=2

    )

    movie2 = Movie(
        id=2,
        title="Одержимость",
        description="Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?",
        trailer="https://www.youtube.com/watch?v=Q9PxDPOo1jw",
        year=2015,
        rating=8.5,
        genre=g2,
        director=d2,
        genre_id=4,
        director_id=8

    )

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) == 2

    def test_create(self):
        movie_d = {
            "description": "События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...",
            "rating": 6.0,
            "id": 3,
            "title": "Вооружен и очень опасен",
            "year": 1978,
            "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo"

        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def update(self, movie_d):
        return self.dao.update(movie_d)


    def test_delete(self):
        self.movie_service.delete(1)
