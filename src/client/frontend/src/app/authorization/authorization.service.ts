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
    this.setClientId();
  }

  setClientId() {
    this.http.get<string>(
      "/assets/client_id.json"
    )
      .subscribe(data => {
        this.clientId = data
      }
    );
  }

  getAuthorizationCode() {
    if (!this.clientId.length) {
      this.setClientId();
    }
    window.location.href = `http://localhost:4201/authorize?client_id=${this.clientId}&response_type=code&redirect_uri=http://localhost:4200&scope=read_potatoes`
    // return this.http.post("http://localhost:8000/authorization-code", {
    //   client_id: this.clientId,
    //   response_type: "code",
    //   redirect_uri: "http://localhost:4200/authorization",
    //   scope: ["potatoes_read"],    
    // })
  }
}
