import { Component } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';

  constructor(
    public userService: UserService,
  ) { }


  loginClicked() {
    this.userService.login(this.email, this.password).subscribe()
  }
}
