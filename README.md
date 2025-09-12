Here’s a well-structured **README.md** for your project:

````markdown
# LLM-Driven Restaurant Finder API

This project is a **FastAPI**-based service that leverages **OpenAI** and **Foursquare Places API** to find restaurants based on natural language queries.  
The application is containerized with Docker, deployed via **Terraform** (IaC), and integrated with **GitHub Actions** for CI/CD.

---

## 🚀 Features

- **Healthcheck**
  - `GET /api/ping` – Simple ping endpoint to verify that the API is running.

- **Restaurant Finder**
  - `POST /api/execute`
    - Accepts a natural language message (e.g., *“Find me Japanese restaurants near Manila with good ratings”*).
    - Calls **OpenAI** to parse the message into a structured JSON request accepted by **Foursquare Places API**.
    - Returns a standardized **Restaurant DTO**:

      ```python
      class RestaurantDto(BaseModel):
          name: str
          cuisine: str
          address: str
          operating_hours: str | None = None
          rating: float | None = None
          price_level: int | None = None
      ```

- **Infrastructure**
  - **Terraform** for infrastructure as code (`/infra`).
  - **GitHub Actions** for automated builds & pushing Docker images to **ECR**.
  - Optional **CloudWatch** support.

- **Domain**
  - Configured with **DuckDNS** for custom domain setup.

---

## 🛠️ Local Development

### Requirements
- Python 3.10+
- [Poetry](https://python-poetry.org/) for dependency management
- Docker (for containerized builds)
- Terraform (if you want to deploy infra)
- OpenAI and Foursquare API keys (for `/api/execute`)

### Setup
```bash
# Install dependencies
poetry install

# Activate virtual environment
$(poetry env activate)

# Run the app
python -m app
````

The API will be available at [http://localhost:8000](http://localhost:8000).
Interactive Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing

The project uses **pytest**. Note that you’ll need valid API keys for OpenAI and Foursquare:

```bash
OPENAI_API_KEY=your_key \
FOURSQUARE_SERVICE_KEY=your_key \
pytest -sv
```

---

## 📦 Docker

Build and run with Docker:

```bash
# Build image
docker build -t restaurant-finder-api .

# Run container
docker run --env-file .env -p 8000:8000 restaurant-finder-api
```

## ☁️ Infrastructure

Terraform is used to provision infra in AWS:

```bash
cd infra
terraform init
terraform apply
```

> ⚠️ Don’t forget to build and push the Docker image to **AWS ECR** before applying Terraform.


## 🔑 Environment Variables

| Variable                 | Description                               | Required |
|---------------------------|-------------------------------------------|----------|
| `OPENAI_API_KEY`          | OpenAI API key                           | ✅       |
| `FOURSQUARE_SERVICE_KEY`  | Foursquare API key                       | ✅       |
| `CW_LOG_GROUP_NAME`       | CloudWatch Log Group name                | ❌       |
| `CW_NAMESPACE`            | CloudWatch namespace for custom metrics  | ❌       |
| `INSTANCE_ID`             | EC2/ECS instance identifier for metrics  | ❌       |

## 🌐 Domain

This project uses **DuckDNS** for domain management. Update DNS accordingly after deployment.

## 📋 Roadmap / Improvements

* [ ] Add caching layer for frequent queries
* [ ] Improve test coverage (mock OpenAI & Foursquare calls)
* [ ] Expand infra to support multi-region deployments
* [ ] Add authentication/authorization
