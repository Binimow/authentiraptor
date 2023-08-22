import { Component } from '@angular/core';
import { AuthorizationCodeService } from '../services/authorization-code.service';

@Component({
  selector: 'app-consent',
  templateUrl: './consent.component.html',
  styleUrls: ['./consent.component.css']
})
export class ConsentComponent {
  constructor(
    public authorizationCodeService : AuthorizationCodeService
  ) { }

  consentGiven() {
    this.authorizationCodeService.getAuthorizationCode().subscribe(
      authorizationCode => {
        if (authorizationCode) {
          window.location.href = `${this.authorizationCodeService.redirectUri}?code=${authorizationCode}`
        }
        else {
          window.location.href = `${this.authorizationCodeService.redirectUri}?error=access_denied`
        }
      }
    )
  }


}
