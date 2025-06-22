require('dotenv').config(); // pulls in .env
const axios = require('axios');

async function getSandboxTransactions() {
  try {
    const response = await axios.post('https://sandbox.plaid.com/transactions/get', {
      client_id: process.env.PLAID_CLIENT_ID,
      secret: process.env.PLAID_SECRET,
      access_token: 'access-sandbox-123xyz', // swap this later
      start_date: '2024-01-01',
      end_date: '2024-01-31'
    });

    console.log(response.data);
  } catch (err) {
    console.error('Something went wrong:', err.response?.data || err.message);
  }
}

getSandboxTransactions();
