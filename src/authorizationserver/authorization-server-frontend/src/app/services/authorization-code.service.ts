import { HttpClient } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserService } from './user.service';
import { catchError, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthorizationCodeService  {
  clientId: string | null = null;
  redirectUri: string | null = null;
  scope: string[] | null = null;

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient,
    private userService: UserService,
  ) {
    this.route.queryParamMap.subscribe(params => {
      console.log(params)
      this.clientId = params.get('client_id');
      this.redirectUri = params.get('redirect_uri');
      this.scope = params.get('scope') ? params.get('scope')!.split(',') : null;
    })
   }

  getAuthorizationCode() {
    const user = this.userService.currentLoggedInUser;
    return this.http.post<string>('http://localhost:8000/authorization-code', {
      user: user,
      client_id: this.clientId,
      redirect_uri: this.redirectUri,
      scope: this.scope,
      response_type: 'code',
    }).pipe(
      catchError(_ => of(null)),
    )
  }

}
