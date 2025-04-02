# Save Documents API

## Objectives
- Use git/github as version control
- Use github action for cicd

### Backend API
- Develop a RESTful API with Flask
- Practice TDD
- Run services Locally with Docker, Docker Compose, Docker Machine
- Host production on AWS(EC2, S3, DBS)


## API Design

| Endpoint | HTTP Method | CRUD Method | Result |
|----------|-------------|-------------|--------|
| /user/login/ | POST    | CREATE      | login user |
| /docs/create/ | POST    | CREATE      | save document|
| /docs    | GET          | READ       | get all documents |
| /docs/:public_id | GET  | READ      | get single document |
| /docs/:public_id | DELETE  | DELETE      | delete single document |