from models.movie import Movie as MovieModel
from schemas.movie import Movie
class MovieService():
    def __init__(self, db):
        self.db = db
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    def get_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).first()
        return result
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
    def delete_movie(self, id: int):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(movie)
        self.db.commit()