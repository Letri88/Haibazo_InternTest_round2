import axios from "axios";

// In Vercel, you will set REACT_APP_API_URL in Environment Variables
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export default axios.create({
  baseURL: API_URL
});