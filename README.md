# Cloud computing & Service architecture(CCSA) project
修習該課程的課堂專案

# QUICKSTART
請先安裝docker
## how to run
```
docker compose up -d
```

## how to test
```
docker compose -f docker-compose.test.yml build
docker compose -f docker-compose.test.yml up -d && docker logs backend_tests
```
