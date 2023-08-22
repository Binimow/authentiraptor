import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../models/user';
import { catchError, map, of, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  currentLoggedInUser: User | null = null;

  constructor(
    private http: HttpClient,
  ) { }

  login(email: string, password: string) {
    return this.http.post<User>('http://localhost:8000/user/login', {
      email: email,
      password: password
    }).pipe(
      catchError(_ => of(null)),
      tap(user => { 
        this.currentLoggedInUser = user;
        if (this.currentLoggedInUser) {
          this.currentLoggedInUser.password = password;
        }
      }),
    )
  }

}
