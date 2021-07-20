# How to run
- Create `.env` file at the root folder with this content

```
POSTGRES_USER=user
POSTGRES_DB=linksapp
POSTGRES_PASSWORD=password
DATABASE_URI='postgresql://user:password@db/linksapp'
DOMAIN_NAME=http://localhost:8000
```
- Run `docker-compose up -d --build`

- Check API docs `http://localhost:8000/docs`

- Get a short url 

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"url":"https://google.com"}' \
  http://localhost:8000/api/urls
```
- Access a shortened url
  ```
  curl  http://localhost:8000/GHO97J2Xne0
  
  ```

## Running tests

- Change the `DATABASE_URI` value to `sqlite:///test.db`
- Run tests with `docker-compose exec app pytest .`


