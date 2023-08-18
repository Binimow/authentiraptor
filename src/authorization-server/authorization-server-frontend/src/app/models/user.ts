export interface User {
    id: number;
    email: string;
    permissions: [];
    password?: string;
}