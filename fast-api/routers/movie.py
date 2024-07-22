from fastapi import APIRouter, Depends
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter(prefix="", tags=["movies"])


@movie_router.get("/movies", tags=["movies"], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    db.close()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get("/movies/{id}", tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    db.close()
    if not result:
        return JSONResponse(content={"message": "Not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get("/movies/", tags=["movies"], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    db.close()
    if not result:
        return JSONResponse(content={"message": f"Not movies found with {category} category"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.post("/movies", tags=["movies"], response_model=dict)
def add_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Movie created"}, status_code=201)


@movie_router.put("/movies/{id}", tags=["movies"], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    exist_movie = MovieService(db).get_movie(id)
    if not exist_movie:
        return JSONResponse(content={"message": "Not found"}, status_code=404)
    MovieService(db).update_movie(id, movie)
    db.close()
    return JSONResponse(content={"message": "Movie updated"}, status_code=200)


@movie_router.delete("/movies/{id}", tags=["movies"], response_model=dict)
def delete_movie(id: int) -> dict:
    db = Session()
    exist_movie = MovieService(db).get_movie(id)
    if not exist_movie:
        return JSONResponse(content={"message": "Not found"}, status_code=404)
    MovieService(db).delete_movie(id)
    db.close()
    return JSONResponse(content={"message": "Movie deleted"}, status_code=204)
