// src/api/auth.ts
import { apiRequest } from "./client";

export interface LoginData {
  username: string;   // или email — как у вас в бэкенде
  password: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export async function login(data: LoginData): Promise<TokenResponse> {
  return apiRequest<TokenResponse>("/auth/login", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function register(data: LoginData): Promise<unknown> {
  return apiRequest("/auth/register", {
    method: "POST",
    body: JSON.stringify(data),
  });
}