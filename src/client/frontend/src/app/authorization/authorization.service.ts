import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthorizationService {

  clientId: string = "";

  constructor(
    private http: HttpClient
  ) {

  }

  setClientId() {
    this.http.get<{clientId: string}>(
      "/assets/client_id.json"
    ).subscribe(
      (data: {clientId: string}) => {
        console.log(data);
        this.clientId = this.clientId
      }
    );
  }

  getAuthorizationCode() {
    if (!this.clientId.length) {
      this.setClientId();
    }
    return this.http.post("http://localhost:8000/pre_getauthorizationcode", {
      client_id: this.clientId,
      response_type: "code",
      redirect_uri: "http://localhost:4200/authorization",
      scopes: ["potatoes_read"],    
    })
  }
}
