import { Component } from '@angular/core';
import { AuthorizationService } from '../authorization.service';

@Component({
  selector: 'app-access-token-button',
  templateUrl: './access-token-button.component.html',
  styleUrls: ['./access-token-button.component.css']
})
export class GetAccessTokenComponent {
  constructor(
    private authorizationService: AuthorizationService
  ) {

  }

  getAuthorizationCode() {
    this.authorizationService.getAuthorizationCode().subscribe(authorizationCode => {
      console.log(authorizationCode);
    })
  }
}
