# Analytics API

Welcome to the Analytics API project! This repository provides a robust and scalable API designed to facilitate seamless data analytics operations. Whether you're building data-driven applications or integrating analytics into existing systems, this API offers the flexibility and performance you need.

## Features

- **Comprehensive Data Endpoints**: Access a wide range of data analytics functionalities through well-defined endpoints.
- **Scalability**: Designed to handle large datasets efficiently, ensuring optimal performance.
- **Extensibility**: Easily customizable to fit specific analytics requirements and workflows.
- **Docker Support**: Simplified deployment using Docker, allowing for consistent environments across development and production.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started): For containerization and simplified deployment.
- [Docker Compose](https://docs.docker.com/compose/install/): To manage multi-container Docker applications.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/herman72/analytics-api.git
   cd analytics-api
   ```

2. **Set Up Environment Variables**:

   - Rename `.env.compose` to `.env`:

     ```bash
     mv .env.compose .env
     ```

   - Update the `.env` file with your specific configuration settings.

### Usage

#### Building and Running the Application

Utilize Docker Compose for streamlined management:

- **Start the Application**:

  ```bash
  docker compose up --watch
  ```

  This command builds the Docker image and starts the application in detached mode.

- **Stop the Application**:

  ```bash
  docker compose down
  ```

  To remove associated volumes:

  ```bash
  docker compose down -v
  ```

#### Accessing the Application

Once the application is running, access the API documentation and test endpoints by navigating to `http://localhost:8000` in your browser.

## Development

For development purposes, you can access the application container's shell:

```bash
docker compose run app /bin/bash
```

Or, to start a Python interactive session:

```bash
docker compose run app python
```

## Contributing

We welcome contributions to enhance the Analytics API. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for more details.

---

For any questions or further assistance, feel free to open an issue in this repository. Happy coding! 






Docker
- `docker build -t analytics-app -f Dockerfile.web .`
- `docker run analytics-app`

becomes

- `docker compose run app /bin/bash` or `docker compose run app python` 
