# Payment System API (BI_PAY)

Welcome to the Payment System API documentation. This API allows the receiver to be in control of the payment process by manually approving received payments.

![Sample Image](https://github.com/Levi-Chinecherem/payment-system-api/blob/main/static/sample.png)

## API Endpoints

### 1. Retrieve the Most Recently Added USDT TRC20 Payment Details

- **Endpoint:** `/api/v1/usdt-trc20/`
- **Method:** `GET`
- **Description:** Retrieve the details of the most recently added USDT TRC20 payment.
- **Response:**
  - Status Code: `200 OK`
  - Body: JSON representation of the USDT TRC20 payment details.

### 2. Retrieve the Most Recently Added USDT ERC20 Payment Details

- **Endpoint:** `/api/v1/usdt-erc20/`
- **Method:** `GET`
- **Description:** Retrieve the details of the most recently added USDT ERC20 payment.
- **Response:**
  - Status Code: `200 OK`
  - Body: JSON representation of the USDT ERC20 payment details.

### 3. Retrieve the Most Recently Added BTC Payment Details

- **Endpoint:** `/api/v1/btc/`
- **Method:** `GET`
- **Description:** Retrieve the details of the most recently added BTC payment.
- **Response:**
  - Status Code: `200 OK`
  - Body: JSON representation of the BTC payment details.

## API Documentation

For detailed API documentation and interactive testing, you can use the following links:

- [Swagger UI](http://localhost:8000/swagger/): Explore and test the API using Swagger UI.
- [ReDoc](http://localhost:8000/redoc/): An alternative API documentation interface.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/payment-system-api.git

   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:

   ```bash
   python manage.py runserver
   ```
4. Access the API endpoints:

   - USDT TRC20: [http://localhost:8000/api/v1/usdt-trc20/](http://localhost:8000/api/v1/usdt-trc20/)
   - USDT ERC20: [http://localhost:8000/api/v1/usdt-erc20/](http://localhost:8000/api/v1/usdt-erc20/)
   - BTC: [http://localhost:8000/api/v1/btc/](http://localhost:8000/api/v1/btc/)

## Important Notes

- This API is currently in development, and the endpoints may change in future versions.
- Ensure that you have the necessary permissions to access and modify payment details.
- For any issues or questions, please contact us at [mail](mailto:lchinecherem2018@gmail.com).


