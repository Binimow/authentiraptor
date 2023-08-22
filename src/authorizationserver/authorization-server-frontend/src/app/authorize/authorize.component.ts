import { Component } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-authorize',
  templateUrl: './authorize.component.html',
  styleUrls: ['./authorize.component.css']
})
export class AuthorizeComponent {
  constructor(public userService: UserService) { }
}
