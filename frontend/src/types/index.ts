export interface DashboardStats {
  total_customers: number;
  active_policies: number;
  upcoming_renewals: number;
}

export interface Customer {
  id: number;
  name: string;
  email?: string;
  phone?: string;
  address?: string;
  notes?: string;
  created_at: string;
}

export interface CustomerCreate {
  name: string;
  email?: string;
  phone?: string;
  address?: string;
  notes?: string;
}

export interface Insurance {
  id: number;
  customer_id: number;
  policy_number: string;
  provider: string;
  type: string;
  start_date: string;
  end_date: string;
  premium_amount: number;
  coverage_amount: number;
  status: string;
  notes?: string;
  created_at: string;
}

export interface Document {
  id: number;
  customer_id: number;
  insurance_id?: number;
  filename: string;
  file_path: string;
  created_at: string;
} 