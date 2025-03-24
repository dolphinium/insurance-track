import axios from 'axios';
import { Customer, DashboardStats } from '../types';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle common errors here
    if (error.response) {
      // Server responded with error status
      console.error('API Error:', error.response.data);
    } else if (error.request) {
      // Request made but no response received
      console.error('Network Error:', error.request);
    } else {
      // Error in request configuration
      console.error('Request Error:', error.message);
    }
    return Promise.reject(error);
  }
);

// Updated ApiResponse to extend the actual data type
export type ApiResponse<T> = T & {
  message: string | null;
};

export interface Insurance {
  id: number;
  customer_id: number;
  type: string;
  renewal_date: string;
  coverage_details: string;
  premium_amount: number;
  notes: string;
  created_at: string;
}

export interface InsuranceCreate {
  customer_id: number;
  type: string;
  renewal_date: string;
  coverage_details: string;
  premium_amount: number;
  notes: string;
}

// API endpoints
export const endpoints = {
  dashboard: {
    stats: () => api.get<ApiResponse<DashboardStats>>('/dashboard/stats'),
  },
  customers: {
    list: () => api.get<ApiResponse<Customer[]>>('/customers'),
    get: (id: number) => api.get<ApiResponse<Customer>>(`/customers/${id}`),
    create: (data: Partial<Customer>) => api.post<ApiResponse<Customer>>('/customers', data),
    update: (id: number, data: Partial<Customer>) => api.put<ApiResponse<Customer>>(`/customers/${id}`, data),
    delete: (id: number) => api.delete<ApiResponse<void>>(`/customers/${id}`),
  },
  insurances: {
    list: () => api.get<Insurance[]>('/insurances'),
    get: (id: number) => api.get<Insurance>(`/insurances/${id}`),
    getCustomerInsurances: (customerId: number) => api.get<Insurance[]>(`/insurances/customer/${customerId}`),
    create: (data: InsuranceCreate) => api.post<Insurance>('/insurances', data),
    update: (id: number, data: Partial<InsuranceCreate>) => api.put<Insurance>(`/insurances/${id}`, data),
    delete: (id: number) => api.delete<void>(`/insurances/${id}`),
  },
};

export default api; 